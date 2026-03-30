# Raspberry Pi Shrimp Farm Dashboard

A Python-based monitoring dashboard for Raspberry Pi. Reads sensor data (from ESP32 via MQTT or direct GPIO sensors), stores history in SQLite, serves a web dashboard, and sends alerts via email/Telegram.

## Architecture

```
Sensors (ESP32/Arduino) --MQTT--> Raspberry Pi ---> SQLite DB
                                       |
                                       +--> Web Dashboard (Flask)
                                       +--> Alerts (Email/Telegram)
                                       +--> CSV Export
```

## Hardware Options

### Option A: Pi as Hub (recommended)
- ESP32 reads sensors and publishes to MQTT
- Pi runs MQTT broker (Mosquitto) + dashboard + alerting
- Multiple ESP32 units for multiple tanks

### Option B: Direct GPIO Sensors
- Sensors wired directly to Pi GPIO
- Simpler for single-tank setups
- Requires ADC hat (MCP3008) for analog sensors

## Software Requirements

```bash
pip install flask flask-socketio paho-mqtt sqlite3 matplotlib
sudo apt install mosquitto mosquitto-clients
```

## Quick Start

```bash
# 1. Clone this repo
git clone <repo-url>
cd hardware/raspberry-pi

# 2. Edit configuration
cp config.example.py config.py
nano config.py  # Set your MQTT, alert, and threshold settings

# 3. Start the dashboard
python dashboard.py

# 4. Open browser to http://<pi-ip>:5000
```

## Features

- Real-time parameter display (updates every 30 seconds)
- Historical charts (24h, 7d, 30d views)
- Alert thresholds with email/Telegram notifications
- Multi-tank support
- CSV data export for analysis
- Mobile-responsive web interface
