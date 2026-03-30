# Arduino/ESP32 Shrimp Tank Water Monitor

A WiFi-connected water quality monitoring system built on ESP32. Reads pH, temperature, and dissolved oxygen, logs data, and sends alerts when parameters go out of range.

## Hardware Required

| Component | Model | Approx Cost | Notes |
|-----------|-------|-------------|-------|
| Microcontroller | ESP32 DevKit | $8-15 | Built-in WiFi + Bluetooth |
| pH Sensor | DFRobot Gravity Analog pH Sensor V2 | $30-40 | Includes probe + signal board |
| Temperature | DS18B20 Waterproof Probe | $3-8 | OneWire protocol, accurate to ±0.5°C |
| TDS Sensor | DFRobot Gravity TDS Sensor | $12-18 | For salinity/TDS estimation |
| DO Sensor (optional) | DFRobot Gravity DO Sensor | $60-80 | Most expensive, but critical |
| OLED Display | SSD1306 128x64 I2C | $5-8 | Local readout |
| Buzzer | Piezo buzzer 5V | $1-2 | Audible alerts |
| Power | 5V USB power supply | $5-10 | Reliable supply critical |
| Breadboard + Wires | Standard kit | $10 | For prototyping |

**Total cost: ~$75-180** depending on sensors selected.

## Wiring

```
ESP32 Pin Assignments:
  GPIO 34 (ADC1_CH6) -> pH Sensor analog out
  GPIO 35 (ADC1_CH7) -> TDS Sensor analog out
  GPIO 36 (ADC1_CH0) -> DO Sensor analog out (if used)
  GPIO 4              -> DS18B20 data (with 4.7K pullup to 3.3V)
  GPIO 21 (SDA)       -> OLED SDA
  GPIO 22 (SCL)       -> OLED SCL
  GPIO 25             -> Buzzer
  3.3V                -> Sensors VCC (check individual sensor voltage!)
  GND                 -> Common ground
```

## Software Setup

1. Install Arduino IDE or PlatformIO
2. Install ESP32 board support
3. Install libraries:
   - `OneWire` (for DS18B20)
   - `DallasTemperature` (for DS18B20)
   - `Adafruit_SSD1306` (for OLED)
   - `WiFi` (built into ESP32)
   - `HTTPClient` (built into ESP32)
4. Copy `shrimp-monitor.ino` to your project
5. Edit WiFi credentials and alert thresholds
6. Upload and go

## Features

- Reads pH, temperature, TDS every 30 seconds
- Displays current values on OLED
- Buzzer alarm when any parameter goes out of range
- Sends data to ThingSpeak (free IoT platform) every 5 minutes
- Serial output for debugging
- Configurable alert thresholds per species

## Calibration

**pH Sensor**: Use pH 4.0 and pH 7.0 calibration solutions. Follow DFRobot calibration procedure.

**Temperature**: DS18B20 is factory calibrated. Verify against a known-good thermometer.

**TDS**: Calibrate with known TDS solution (usually 1000 ppm included with sensor).
