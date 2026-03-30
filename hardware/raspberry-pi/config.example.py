"""
Shrimp Farm Dashboard Configuration
Copy this to config.py and edit for your setup.
"""

# ─────────────────────────────────────────────────────────────────────
# MQTT Settings (for receiving data from ESP32 sensors)
# ─────────────────────────────────────────────────────────────────────
MQTT_BROKER = "localhost"      # Or IP of your MQTT broker
MQTT_PORT = 1883
MQTT_TOPIC_PREFIX = "shrimp/"  # Topics: shrimp/tank1/temp, shrimp/tank1/ph, etc.

# ─────────────────────────────────────────────────────────────────────
# Tank Configuration
# ─────────────────────────────────────────────────────────────────────
TANKS = {
    "tank1": {
        "name": "IBC Tote #1 - Vannamei",
        "species": "vannamei",
        "volume_gallons": 275,
    },
    "tank2": {
        "name": "IBC Tote #2 - Vannamei",
        "species": "vannamei",
        "volume_gallons": 275,
    },
}

# ─────────────────────────────────────────────────────────────────────
# Alert Thresholds (per species)
# ─────────────────────────────────────────────────────────────────────
THRESHOLDS = {
    "vannamei": {
        "temp_min": 26.0, "temp_max": 33.0,
        "ph_min": 7.0, "ph_max": 9.0,
        "tds_min": 10000, "tds_max": 30000,
        "do_min": 4.0,
    },
    "neocaridina": {
        "temp_min": 18.0, "temp_max": 28.0,
        "ph_min": 6.5, "ph_max": 8.0,
        "tds_min": 150, "tds_max": 350,
        "do_min": 4.0,
    },
    "caridina": {
        "temp_min": 18.0, "temp_max": 25.0,
        "ph_min": 5.5, "ph_max": 7.0,
        "tds_min": 80, "tds_max": 220,
        "do_min": 5.0,
    },
}

# ─────────────────────────────────────────────────────────────────────
# Alert Settings
# ─────────────────────────────────────────────────────────────────────
ALERT_COOLDOWN_MINUTES = 30  # Don't re-alert for same issue within this window

# Email alerts (optional)
EMAIL_ENABLED = False
EMAIL_SMTP_HOST = "smtp.gmail.com"
EMAIL_SMTP_PORT = 587
EMAIL_FROM = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"  # Use Gmail App Password
EMAIL_TO = "your-email@gmail.com"

# Telegram alerts (optional)
TELEGRAM_ENABLED = False
TELEGRAM_BOT_TOKEN = "your-bot-token"
TELEGRAM_CHAT_ID = "your-chat-id"

# ─────────────────────────────────────────────────────────────────────
# Database
# ─────────────────────────────────────────────────────────────────────
DATABASE_PATH = "shrimp_data.db"
DATA_RETENTION_DAYS = 365  # Keep data for 1 year

# ─────────────────────────────────────────────────────────────────────
# Web Dashboard
# ─────────────────────────────────────────────────────────────────────
DASHBOARD_HOST = "0.0.0.0"
DASHBOARD_PORT = 5000
