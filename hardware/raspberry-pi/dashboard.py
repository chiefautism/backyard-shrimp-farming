#!/usr/bin/env python3
"""
Shrimp Farm Monitoring Dashboard

A Flask-based web dashboard that:
- Receives sensor data via MQTT from ESP32 monitors
- Stores readings in SQLite
- Serves a real-time web dashboard
- Sends alerts when parameters go out of range
"""

import json
import sqlite3
import smtplib
import time
import threading
from datetime import datetime, timedelta
from email.mime.text import MIMEText

from flask import Flask, jsonify, render_template_string, request
import paho.mqtt.client as mqtt

try:
    from config import *
except ImportError:
    print("ERROR: config.py not found. Copy config.example.py to config.py and edit it.")
    exit(1)

# ─────────────────────────────────────────────────────────────────────
# Database
# ─────────────────────────────────────────────────────────────────────

def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS readings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tank_id TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            temperature REAL,
            ph REAL,
            tds REAL,
            do_level REAL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tank_id TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            parameter TEXT,
            value REAL,
            threshold_min REAL,
            threshold_max REAL,
            message TEXT
        )
    """)
    conn.execute("""
        CREATE INDEX IF NOT EXISTS idx_readings_tank_time
        ON readings(tank_id, timestamp)
    """)
    conn.commit()
    conn.close()


def save_reading(tank_id, temperature=None, ph=None, tds=None, do_level=None):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.execute(
        "INSERT INTO readings (tank_id, temperature, ph, tds, do_level) VALUES (?, ?, ?, ?, ?)",
        (tank_id, temperature, ph, tds, do_level)
    )
    conn.commit()
    conn.close()


def get_readings(tank_id, hours=24):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    since = datetime.utcnow() - timedelta(hours=hours)
    rows = conn.execute(
        "SELECT * FROM readings WHERE tank_id = ? AND timestamp > ? ORDER BY timestamp",
        (tank_id, since.isoformat())
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_latest_reading(tank_id):
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute(
        "SELECT * FROM readings WHERE tank_id = ? ORDER BY timestamp DESC LIMIT 1",
        (tank_id,)
    ).fetchone()
    conn.close()
    return dict(row) if row else None


def cleanup_old_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cutoff = datetime.utcnow() - timedelta(days=DATA_RETENTION_DAYS)
    conn.execute("DELETE FROM readings WHERE timestamp < ?", (cutoff.isoformat(),))
    conn.execute("DELETE FROM alerts WHERE timestamp < ?", (cutoff.isoformat(),))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────────────────────────────────
# MQTT
# ─────────────────────────────────────────────────────────────────────

# Store latest values per tank
latest_data = {}
alert_cooldowns = {}


def on_mqtt_connect(client, userdata, flags, rc):
    print(f"MQTT connected (rc={rc})")
    client.subscribe(f"{MQTT_TOPIC_PREFIX}#")


def on_mqtt_message(client, userdata, msg):
    """
    Expected topic format: shrimp/tank1/temp, shrimp/tank1/ph, etc.
    Payload: numeric value as string
    """
    try:
        parts = msg.topic.replace(MQTT_TOPIC_PREFIX, "").split("/")
        if len(parts) < 2:
            return

        tank_id = parts[0]
        param = parts[1]
        value = float(msg.payload.decode())

        if tank_id not in latest_data:
            latest_data[tank_id] = {"timestamp": datetime.utcnow().isoformat()}

        latest_data[tank_id][param] = value
        latest_data[tank_id]["timestamp"] = datetime.utcnow().isoformat()

        # Save complete reading when we have all params
        data = latest_data[tank_id]
        if all(k in data for k in ["temp", "ph", "tds"]):
            save_reading(
                tank_id,
                temperature=data.get("temp"),
                ph=data.get("ph"),
                tds=data.get("tds"),
                do_level=data.get("do"),
            )
            check_alerts(tank_id, data)

    except (ValueError, IndexError) as e:
        print(f"MQTT parse error: {e} (topic={msg.topic})")


def check_alerts(tank_id, data):
    tank_config = TANKS.get(tank_id, {})
    species = tank_config.get("species", "vannamei")
    thresholds = THRESHOLDS.get(species, {})

    alerts = []

    if "temp" in data and "temp_min" in thresholds:
        if data["temp"] < thresholds["temp_min"]:
            alerts.append(f"Temperature LOW: {data['temp']:.1f}°C (min: {thresholds['temp_min']})")
        elif data["temp"] > thresholds["temp_max"]:
            alerts.append(f"Temperature HIGH: {data['temp']:.1f}°C (max: {thresholds['temp_max']})")

    if "ph" in data and "ph_min" in thresholds:
        if data["ph"] < thresholds["ph_min"]:
            alerts.append(f"pH LOW: {data['ph']:.2f} (min: {thresholds['ph_min']})")
        elif data["ph"] > thresholds["ph_max"]:
            alerts.append(f"pH HIGH: {data['ph']:.2f} (max: {thresholds['ph_max']})")

    if "tds" in data and "tds_min" in thresholds:
        if data["tds"] < thresholds["tds_min"]:
            alerts.append(f"TDS LOW: {data['tds']:.0f} (min: {thresholds['tds_min']})")
        elif data["tds"] > thresholds["tds_max"]:
            alerts.append(f"TDS HIGH: {data['tds']:.0f} (max: {thresholds['tds_max']})")

    for alert_msg in alerts:
        cooldown_key = f"{tank_id}:{alert_msg[:20]}"
        now = time.time()
        if cooldown_key in alert_cooldowns:
            if now - alert_cooldowns[cooldown_key] < ALERT_COOLDOWN_MINUTES * 60:
                continue
        alert_cooldowns[cooldown_key] = now

        tank_name = tank_config.get("name", tank_id)
        full_msg = f"[{tank_name}] {alert_msg}"
        print(f"ALERT: {full_msg}")
        send_alert(full_msg)


def send_alert(message):
    if EMAIL_ENABLED:
        try:
            msg = MIMEText(message)
            msg["Subject"] = "Shrimp Farm Alert"
            msg["From"] = EMAIL_FROM
            msg["To"] = EMAIL_TO
            with smtplib.SMTP(EMAIL_SMTP_HOST, EMAIL_SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_FROM, EMAIL_PASSWORD)
                server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        except Exception as e:
            print(f"Email alert failed: {e}")

    if TELEGRAM_ENABLED:
        try:
            import requests
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
            requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": message})
        except Exception as e:
            print(f"Telegram alert failed: {e}")


# ─────────────────────────────────────────────────────────────────────
# Web Dashboard
# ─────────────────────────────────────────────────────────────────────

app = Flask(__name__)

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Shrimp Farm Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
               background: #0a0e17; color: #e0e0e0; padding: 20px; }
        h1 { text-align: center; color: #4fc3f7; margin-bottom: 20px; font-size: 1.5em; }
        .tanks { display: flex; flex-wrap: wrap; gap: 20px; justify-content: center; }
        .tank-card {
            background: #1a1e2e; border-radius: 12px; padding: 20px;
            min-width: 300px; flex: 1; max-width: 500px;
            border: 1px solid #2a3050;
        }
        .tank-name { font-size: 1.1em; color: #4fc3f7; margin-bottom: 15px; }
        .param {
            display: flex; justify-content: space-between; align-items: center;
            padding: 8px 0; border-bottom: 1px solid #1e2540;
        }
        .param-label { color: #888; font-size: 0.9em; }
        .param-value { font-size: 1.3em; font-weight: bold; }
        .ok { color: #66bb6a; }
        .warn { color: #ffa726; }
        .alert { color: #ef5350; animation: blink 1s infinite; }
        @keyframes blink { 50% { opacity: 0.5; } }
        .timestamp { color: #555; font-size: 0.8em; margin-top: 10px; text-align: right; }
        .no-data { color: #555; text-align: center; padding: 40px; }
        .refresh-note { text-align: center; color: #444; margin-top: 20px; font-size: 0.8em; }
    </style>
</head>
<body>
    <h1>Shrimp Farm Dashboard</h1>
    <div class="tanks" id="tanks"></div>
    <div class="refresh-note">Auto-refreshes every 30 seconds</div>
    <script>
        function getClass(value, min, max) {
            if (value === null || value === undefined) return '';
            if (value < min || value > max) return 'alert';
            const range = max - min;
            if (value < min + range * 0.1 || value > max - range * 0.1) return 'warn';
            return 'ok';
        }
        function update() {
            fetch('/api/status')
                .then(r => r.json())
                .then(data => {
                    const container = document.getElementById('tanks');
                    container.innerHTML = '';
                    if (Object.keys(data.tanks).length === 0) {
                        container.innerHTML = '<div class="no-data">No tank data yet. Waiting for sensor readings...</div>';
                        return;
                    }
                    for (const [id, tank] of Object.entries(data.tanks)) {
                        const t = tank.thresholds || {};
                        const r = tank.latest || {};
                        const card = document.createElement('div');
                        card.className = 'tank-card';
                        card.innerHTML = `
                            <div class="tank-name">${tank.name || id}</div>
                            <div class="param">
                                <span class="param-label">Temperature</span>
                                <span class="param-value ${getClass(r.temperature, t.temp_min, t.temp_max)}">
                                    ${r.temperature !== null ? r.temperature.toFixed(1) + ' °C' : '--'}
                                </span>
                            </div>
                            <div class="param">
                                <span class="param-label">pH</span>
                                <span class="param-value ${getClass(r.ph, t.ph_min, t.ph_max)}">
                                    ${r.ph !== null ? r.ph.toFixed(2) : '--'}
                                </span>
                            </div>
                            <div class="param">
                                <span class="param-label">TDS</span>
                                <span class="param-value ${getClass(r.tds, t.tds_min, t.tds_max)}">
                                    ${r.tds !== null ? Math.round(r.tds) + ' ppm' : '--'}
                                </span>
                            </div>
                            ${r.do_level !== null && r.do_level !== undefined ? `
                            <div class="param">
                                <span class="param-label">Dissolved O₂</span>
                                <span class="param-value ${getClass(r.do_level, t.do_min, 20)}">
                                    ${r.do_level.toFixed(1)} mg/L
                                </span>
                            </div>` : ''}
                            <div class="timestamp">Last update: ${r.timestamp || 'never'}</div>
                        `;
                        container.appendChild(card);
                    }
                })
                .catch(e => console.error('Update failed:', e));
        }
        update();
        setInterval(update, 30000);
    </script>
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(DASHBOARD_HTML)


@app.route("/api/status")
def api_status():
    result = {"tanks": {}}
    for tank_id, tank_config in TANKS.items():
        species = tank_config.get("species", "vannamei")
        latest = get_latest_reading(tank_id)
        result["tanks"][tank_id] = {
            "name": tank_config.get("name", tank_id),
            "species": species,
            "thresholds": THRESHOLDS.get(species, {}),
            "latest": latest,
        }
    return jsonify(result)


@app.route("/api/history/<tank_id>")
def api_history(tank_id):
    hours = request.args.get("hours", 24, type=int)
    readings = get_readings(tank_id, hours=hours)
    return jsonify({"tank_id": tank_id, "hours": hours, "readings": readings})


@app.route("/api/export/<tank_id>")
def api_export(tank_id):
    hours = request.args.get("hours", 168, type=int)  # Default 7 days
    readings = get_readings(tank_id, hours=hours)
    csv_lines = ["timestamp,temperature,ph,tds,do_level"]
    for r in readings:
        csv_lines.append(
            f"{r['timestamp']},{r.get('temperature','')},{r.get('ph','')},{r.get('tds','')},{r.get('do_level','')}"
        )
    return "\n".join(csv_lines), 200, {
        "Content-Type": "text/csv",
        "Content-Disposition": f"attachment; filename={tank_id}_data.csv"
    }


# ─────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────

def main():
    print("Initializing database...")
    init_db()

    print("Starting MQTT client...")
    mqtt_client = mqtt.Client()
    mqtt_client.on_connect = on_mqtt_connect
    mqtt_client.on_message = on_mqtt_message

    try:
        mqtt_client.connect(MQTT_BROKER, MQTT_PORT)
        mqtt_client.loop_start()
    except Exception as e:
        print(f"MQTT connection failed: {e}")
        print("Dashboard will run without live sensor data.")

    # Run daily cleanup in background
    def daily_cleanup():
        while True:
            time.sleep(86400)  # 24 hours
            cleanup_old_data()
            print("Old data cleaned up")

    cleanup_thread = threading.Thread(target=daily_cleanup, daemon=True)
    cleanup_thread.start()

    print(f"Starting dashboard at http://{DASHBOARD_HOST}:{DASHBOARD_PORT}")
    app.run(host=DASHBOARD_HOST, port=DASHBOARD_PORT, debug=False)


if __name__ == "__main__":
    main()
