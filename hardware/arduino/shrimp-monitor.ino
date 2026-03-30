/*
 * Shrimp Tank Water Quality Monitor
 *
 * Hardware: ESP32 + pH sensor + DS18B20 + TDS sensor + OLED display
 * Features: Real-time monitoring, WiFi logging to ThingSpeak, audible alerts
 *
 * Wiring: See README.md for pin assignments
 */

#include <WiFi.h>
#include <HTTPClient.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// ─────────────────────────────────────────────────────────────────────
// CONFIGURATION - Edit these for your setup
// ─────────────────────────────────────────────────────────────────────

// WiFi
const char* WIFI_SSID     = "YOUR_WIFI_SSID";
const char* WIFI_PASSWORD  = "YOUR_WIFI_PASSWORD";

// ThingSpeak (free IoT platform - create account at thingspeak.com)
const char* THINGSPEAK_API_KEY = "YOUR_WRITE_API_KEY";
const char* THINGSPEAK_HOST    = "http://api.thingspeak.com/update";

// Species presets - uncomment ONE
// Vannamei (saltwater/brackish)
float TEMP_MIN = 26.0, TEMP_MAX = 33.0;
float PH_MIN = 7.0, PH_MAX = 9.0;
float TDS_MIN = 10000, TDS_MAX = 25000;  // ~15-25 ppt salinity

// // Neocaridina (freshwater ornamental)
// float TEMP_MIN = 18.0, TEMP_MAX = 28.0;
// float PH_MIN = 6.5, PH_MAX = 8.0;
// float TDS_MIN = 150, TDS_MAX = 350;

// // Caridina (soft water ornamental)
// float TEMP_MIN = 18.0, TEMP_MAX = 25.0;
// float PH_MIN = 5.5, PH_MAX = 7.0;
// float TDS_MIN = 80, TDS_MAX = 220;

// ─────────────────────────────────────────────────────────────────────
// PIN DEFINITIONS
// ─────────────────────────────────────────────────────────────────────

#define PH_PIN          34    // Analog input for pH sensor
#define TDS_PIN         35    // Analog input for TDS sensor
#define TEMP_PIN         4    // DS18B20 data pin
#define BUZZER_PIN      25    // Piezo buzzer
#define OLED_SDA        21
#define OLED_SCL        22

// ─────────────────────────────────────────────────────────────────────
// CONSTANTS
// ─────────────────────────────────────────────────────────────────────

#define SCREEN_WIDTH    128
#define SCREEN_HEIGHT    64
#define OLED_RESET       -1

#define READ_INTERVAL   30000   // Read sensors every 30 seconds
#define LOG_INTERVAL    300000  // Log to ThingSpeak every 5 minutes
#define NUM_SAMPLES     20      // ADC samples to average

// pH calibration values (adjust after calibrating with buffer solutions)
// Default: linear mapping from voltage to pH
// Calibrate with pH 4.0 and pH 7.0 solutions
float PH_OFFSET = 0.0;       // Calibration offset
float PH_SLOPE  = -5.7;      // mV per pH unit (typical for analog pH sensor)
float PH_NEUTRAL_VOLTAGE = 1500.0;  // mV at pH 7.0 (calibrate this!)

// TDS calibration
float TDS_FACTOR = 0.5;      // Conversion factor (calibrate with known solution)

// ─────────────────────────────────────────────────────────────────────
// GLOBALS
// ─────────────────────────────────────────────────────────────────────

OneWire oneWire(TEMP_PIN);
DallasTemperature tempSensor(&oneWire);
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

float currentTemp = 0;
float currentPH = 0;
float currentTDS = 0;

unsigned long lastReadTime = 0;
unsigned long lastLogTime = 0;
bool alertActive = false;

// ─────────────────────────────────────────────────────────────────────
// SETUP
// ─────────────────────────────────────────────────────────────────────

void setup() {
    Serial.begin(115200);
    Serial.println("\n=== Shrimp Tank Monitor Starting ===");

    // Initialize pins
    pinMode(BUZZER_PIN, OUTPUT);
    digitalWrite(BUZZER_PIN, LOW);

    // Initialize temperature sensor
    tempSensor.begin();
    Serial.println("Temperature sensor initialized");

    // Initialize OLED
    Wire.begin(OLED_SDA, OLED_SCL);
    if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
        Serial.println("OLED init failed!");
    } else {
        display.clearDisplay();
        display.setTextSize(1);
        display.setTextColor(SSD1306_WHITE);
        display.setCursor(0, 0);
        display.println("Shrimp Monitor");
        display.println("Starting...");
        display.display();
        Serial.println("OLED initialized");
    }

    // Connect WiFi
    connectWiFi();

    // Initial read
    readSensors();
    updateDisplay();

    Serial.println("=== Setup Complete ===\n");
}

// ─────────────────────────────────────────────────────────────────────
// MAIN LOOP
// ─────────────────────────────────────────────────────────────────────

void loop() {
    unsigned long now = millis();

    // Read sensors at interval
    if (now - lastReadTime >= READ_INTERVAL) {
        readSensors();
        updateDisplay();
        checkAlerts();
        printSerial();
        lastReadTime = now;
    }

    // Log to ThingSpeak at interval
    if (now - lastLogTime >= LOG_INTERVAL) {
        logToThingSpeak();
        lastLogTime = now;
    }

    delay(100);
}

// ─────────────────────────────────────────────────────────────────────
// SENSOR READING
// ─────────────────────────────────────────────────────────────────────

void readSensors() {
    // Temperature (DS18B20)
    tempSensor.requestTemperatures();
    currentTemp = tempSensor.getTempCByIndex(0);
    if (currentTemp == DEVICE_DISCONNECTED_C) {
        currentTemp = -1;
        Serial.println("WARNING: Temperature sensor disconnected!");
    }

    // pH (analog)
    currentPH = readPH();

    // TDS (analog)
    currentTDS = readTDS();
}

float readPH() {
    // Read multiple samples and average
    long sum = 0;
    for (int i = 0; i < NUM_SAMPLES; i++) {
        sum += analogRead(PH_PIN);
        delay(10);
    }
    float avgADC = (float)sum / NUM_SAMPLES;

    // Convert ADC to voltage (ESP32: 12-bit ADC, 0-3.3V)
    float voltage = avgADC * 3300.0 / 4095.0;  // millivolts

    // Convert voltage to pH
    // pH = 7.0 + (neutralVoltage - voltage) / slope
    float ph = 7.0 + (PH_NEUTRAL_VOLTAGE - voltage) / (PH_SLOPE * -1000.0 / 7.0) + PH_OFFSET;

    // Clamp to valid range
    if (ph < 0) ph = 0;
    if (ph > 14) ph = 14;

    return ph;
}

float readTDS() {
    // Read multiple samples and average
    long sum = 0;
    for (int i = 0; i < NUM_SAMPLES; i++) {
        sum += analogRead(TDS_PIN);
        delay(10);
    }
    float avgADC = (float)sum / NUM_SAMPLES;

    // Convert ADC to voltage
    float voltage = avgADC * 3.3 / 4095.0;

    // Temperature compensation for TDS
    float compensationCoefficient = 1.0 + 0.02 * (currentTemp - 25.0);
    float compensatedVoltage = voltage / compensationCoefficient;

    // Convert to TDS (ppm)
    // Formula from DFRobot TDS sensor
    float tds = (133.42 * compensatedVoltage * compensatedVoltage * compensatedVoltage
                - 255.86 * compensatedVoltage * compensatedVoltage
                + 857.39 * compensatedVoltage) * TDS_FACTOR;

    if (tds < 0) tds = 0;
    return tds;
}

// ─────────────────────────────────────────────────────────────────────
// DISPLAY
// ─────────────────────────────────────────────────────────────────────

void updateDisplay() {
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);

    // Title
    display.setCursor(0, 0);
    display.println("== SHRIMP MONITOR ==");

    // Temperature
    display.setCursor(0, 14);
    display.print("Temp: ");
    if (currentTemp > 0) {
        display.print(currentTemp, 1);
        display.print(" C");
        if (currentTemp < TEMP_MIN || currentTemp > TEMP_MAX) {
            display.print(" !");
        }
    } else {
        display.print("ERROR");
    }

    // pH
    display.setCursor(0, 26);
    display.print("pH:   ");
    display.print(currentPH, 1);
    if (currentPH < PH_MIN || currentPH > PH_MAX) {
        display.print(" !");
    }

    // TDS
    display.setCursor(0, 38);
    display.print("TDS:  ");
    display.print((int)currentTDS);
    display.print(" ppm");
    if (currentTDS < TDS_MIN || currentTDS > TDS_MAX) {
        display.print(" !");
    }

    // Alert status
    display.setCursor(0, 52);
    if (alertActive) {
        display.print(">>> ALERT <<<");
    } else {
        display.print("Status: OK");
    }

    // WiFi indicator
    if (WiFi.status() == WL_CONNECTED) {
        display.setCursor(110, 52);
        display.print("W");
    }

    display.display();
}

// ─────────────────────────────────────────────────────────────────────
// ALERTS
// ─────────────────────────────────────────────────────────────────────

void checkAlerts() {
    bool tempAlert = (currentTemp > 0) && (currentTemp < TEMP_MIN || currentTemp > TEMP_MAX);
    bool phAlert = currentPH < PH_MIN || currentPH > PH_MAX;
    bool tdsAlert = currentTDS < TDS_MIN || currentTDS > TDS_MAX;
    bool tempDisconnected = (currentTemp <= 0);

    alertActive = tempAlert || phAlert || tdsAlert || tempDisconnected;

    if (alertActive) {
        // Beep pattern: 3 short beeps
        for (int i = 0; i < 3; i++) {
            digitalWrite(BUZZER_PIN, HIGH);
            delay(100);
            digitalWrite(BUZZER_PIN, LOW);
            delay(100);
        }

        Serial.print("ALERT: ");
        if (tempAlert)        Serial.print("TEMPERATURE ");
        if (phAlert)          Serial.print("PH ");
        if (tdsAlert)         Serial.print("TDS ");
        if (tempDisconnected) Serial.print("TEMP_SENSOR_ERROR ");
        Serial.println();
    }
}

// ─────────────────────────────────────────────────────────────────────
// DATA LOGGING
// ─────────────────────────────────────────────────────────────────────

void logToThingSpeak() {
    if (WiFi.status() != WL_CONNECTED) {
        Serial.println("WiFi not connected, skipping log");
        connectWiFi();
        return;
    }

    HTTPClient http;
    String url = String(THINGSPEAK_HOST);
    url += "?api_key=" + String(THINGSPEAK_API_KEY);
    url += "&field1=" + String(currentTemp, 2);
    url += "&field2=" + String(currentPH, 2);
    url += "&field3=" + String(currentTDS, 0);

    http.begin(url);
    int httpCode = http.GET();

    if (httpCode > 0) {
        Serial.printf("ThingSpeak: HTTP %d\n", httpCode);
    } else {
        Serial.printf("ThingSpeak error: %s\n", http.errorToString(httpCode).c_str());
    }
    http.end();
}

// ─────────────────────────────────────────────────────────────────────
// WIFI
// ─────────────────────────────────────────────────────────────────────

void connectWiFi() {
    if (WiFi.status() == WL_CONNECTED) return;

    Serial.printf("Connecting to WiFi: %s", WIFI_SSID);
    WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

    int attempts = 0;
    while (WiFi.status() != WL_CONNECTED && attempts < 20) {
        delay(500);
        Serial.print(".");
        attempts++;
    }

    if (WiFi.status() == WL_CONNECTED) {
        Serial.printf("\nConnected! IP: %s\n", WiFi.localIP().toString().c_str());
    } else {
        Serial.println("\nWiFi connection failed. Will retry later.");
    }
}

// ─────────────────────────────────────────────────────────────────────
// SERIAL OUTPUT
// ─────────────────────────────────────────────────────────────────────

void printSerial() {
    Serial.printf("[%lu] Temp=%.1f°C  pH=%.2f  TDS=%.0f ppm  Alert=%s\n",
        millis() / 1000,
        currentTemp,
        currentPH,
        currentTDS,
        alertActive ? "YES" : "no"
    );
}
