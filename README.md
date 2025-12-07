# Home Assistant MQTT Sensor Integration

##  Student Information
- **Name:** SHREE HARINI A
- **Register Number:** 42111225
- **MQTT Topic:** `home/shreeharini-2025/sensor`
- **Date:** December 2025

---

##  Project Overview

This project demonstrates IoT sensor integration using MQTT protocol, connecting Python-based sensor simulation with Home Assistant through a Mosquitto MQTT broker. The system publishes real-time sensor data (temperature, humidity, and light intensity) and displays them in Home Assistant dashboard.

---

##  System Architecture

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────────┐
│  Python Script  │ ──────> │ Mosquitto MQTT   │ ──────> │  Home Assistant     │
│  (Publisher)    │         │    Broker        │         │   (Subscriber)      │
└─────────────────┘         └──────────────────┘         └─────────────────────┘
     Publishes                 Port 1883                    Displays Sensors
   sensor data                Message Router                  in Dashboard
```

---

##  Sensors Implemented

### 1. **Temperature Sensor**
- **Value:** 25°C (fixed)
- **Topic:** `home/shreeharini-2025/sensor/temperature`
- **Unit:** Celsius

### 2. **Humidity Sensor**
- **Value:** 60% (fixed)
- **Topic:** `home/shreeharini-2025/sensor/humidity`
- **Unit:** Percentage

### 3. **Light Intensity Sensor** (Extra Sensor)
- **Value:** 100-1000 lux (randomized)
- **Topic:** `home/shreeharini-2025/sensor/light`
- **Unit:** Lux
- **Purpose:** Simulates ambient light measurement for smart lighting automation
- **Update Rate:** Every 3 seconds

---

##  Technology Stack

- **Python 3.x** - Sensor simulation and MQTT publishing
- **paho-mqtt 2.1.0** - MQTT client library
- **Mosquitto 2.0.18** - MQTT message broker
- **Home Assistant (Docker)** - Smart home automation platform
- **Docker Desktop** - Container runtime for Home Assistant

---

##  Installation & Setup

### Prerequisites
```bash
# Python 3.x installed
# Docker Desktop installed
# Mosquitto MQTT Broker installed
```

### Step 1: Install Python Dependencies
```bash
pip install paho-mqtt
```

### Step 2: Install Mosquitto MQTT Broker
```bash
# Windows: Download from mosquitto.org
# Start the broker
cd C:\Program Files\mosquitto
mosquitto.exe
```

### Step 3: Run Home Assistant in Docker
```bash
docker run -d --name homeassistant -p 8123:8123 --restart unless-stopped ghcr.io/home-assistant/home-assistant:stable
```

### Step 4: Run the Python Script
```bash
python sensor.py
```

---

##  File Structure

```
homeassistant-mqtt-shreeharini/
│
├── sensor.py              # Main Python script
├── README.md              # This file
├── screenshots/
│   ├── sensor_output.png  # Python script output
│   └── mqtt_output.png    # MQTT broker messages
└── assignment_summary.pdf # 1-page summary document
```

---

##  Configuration Details

### MQTT Broker Configuration
- **Host:** `localhost` (or `host.docker.internal` for Docker)
- **Port:** `1883`
- **Protocol:** MQTT v3.1.1
- **QoS Level:** 1 (At least once delivery)
- **Retain Flag:** True

### Home Assistant MQTT Integration
```yaml
mqtt:
  broker: host.docker.internal
  port: 1883
```

---

##  How It Works

1. **Python Script Initialization**
   - Connects to Mosquitto MQTT broker on localhost:1883
   - Establishes persistent connection with unique client ID

2. **Data Publishing**
   - Publishes temperature (25°C) every 3 seconds
   - Publishes humidity (60%) every 3 seconds
   - Publishes light intensity (random 100-1000 lux) every 3 seconds

3. **MQTT Message Flow**
   - Messages published to hierarchical topics
   - Broker routes messages to subscribed clients
   - Home Assistant receives and processes sensor data

4. **Home Assistant Display**
   - MQTT integration configured
   - Sensors automatically discovered
   - Real-time updates displayed on dashboard

---

##  Testing & Verification

### Test MQTT Broker Connection
```bash
# Subscribe to all sensor topics
mosquitto_sub -h localhost -t "home/shreeharini-2025/sensor/#" -v
```

### Expected Output
```
home/shreeharini-2025/sensor/temperature 25
home/shreeharini-2025/sensor/humidity 60
home/shreeharini-2025/sensor/light 543
```

### Verify in Home Assistant
1. Navigate to Developer Tools → MQTT
2. Listen to topic: `home/shreeharini-2025/sensor/#`
3. Observe real-time sensor messages

---

##  Extra Sensor Explanation

### Light Intensity Sensor
The light sensor measures ambient illumination in **lux units**:

- **Range:** 100-1000 lux
- **Typical Values:**
  - 100-300 lux: Dim indoor lighting
  - 300-500 lux: Normal office lighting
  - 500-1000 lux: Bright indoor environment

**Real-World Applications:**
- Automatic blinds control based on sunlight
- Smart lighting systems that adjust brightness
- Energy optimization in smart buildings
- Circadian rhythm lighting automation

---

## 📸 Screenshots

### 1. Python Script Output
Shows successful MQTT connection and continuous sensor data publishing.

### 2. MQTT Broker Messages
Demonstrates message flow through Mosquitto broker with all three sensor topics.

---

## 🎥 Video Demonstration

The video demonstration includes:
- ✅ Face verification with name and register number
- ✅ Real-time system timestamp
- ✅ Python script execution with live output
- ✅ Mosquitto MQTT broker running
- ✅ MQTT messages flowing in terminal
- ✅ Home Assistant dashboard with MQTT integration
- ✅ Source code review showing student credentials

**Duration:** 2-3 minutes

---

##  Key Learning Outcomes

1. **MQTT Protocol Understanding**
   - Publish-Subscribe messaging pattern
   - Topic-based message routing
   - Quality of Service (QoS) levels

2. **IoT System Integration**
   - Sensor data simulation
   - Message broker configuration
   - Smart home platform integration

3. **Docker Container Management**
   - Running Home Assistant in containers
   - Network configuration for localhost access

4. **Python Automation**
   - MQTT client implementation
   - Error handling and connection management
   - Real-time data publishing

---

##  Security Considerations

- Broker runs on localhost (not exposed to internet)
- No authentication configured (suitable for local testing)
- Production systems should implement:
  - Username/password authentication
  - TLS/SSL encryption
  - Access control lists (ACLs)

---

##  Troubleshooting

### Issue: Python script can't connect to MQTT
**Solution:** Verify Mosquitto is running
```bash
# Check if mosquitto is running
netstat -an | findstr 1883
```

### Issue: Home Assistant can't connect to MQTT
**Solution:** Use `host.docker.internal` instead of `localhost` in broker configuration

### Issue: No sensor data in Home Assistant
**Solution:** Check MQTT integration is active in Settings → Devices & Services

---

##  References

- [Home Assistant Documentation](https://www.home-assistant.io/docs/)
- [Mosquitto MQTT Broker](https://mosquitto.org/documentation/)
- [Paho MQTT Python Client](https://pypi.org/project/paho-mqtt/)
- [MQTT Protocol Specification](https://mqtt.org/)

---

##  Assignment Completion Checklist

- [x] Mosquitto MQTT Broker installed and running
- [x] Python script with student name and unique ID
- [x] Unique MQTT topic: `home/shreeharini-2025/sensor`
- [x] Three sensors: temperature, humidity, light
- [x] Home Assistant installed and configured
- [x] MQTT integration successfully connected
- [x] Video recorded with face and timestamp
- [x] Code uploaded to GitHub
- [x] Screenshots captured
- [x] PDF summary document created

---

##  License

This project is created for educational purposes as part of the Nakshatra Automation Home Assistant assignment.

---

##  Author

**SHREE HARINI A**  
Register Number: 42111225  
Nakshatra Automation - Home Assistant MQTT Integration Assignment

---

##  Acknowledgments

Assignment completed independently without collaboration, as per Nakshatra Automation guidelines.

---

**Note:** All work in this repository is original and completed individually for the purpose of technical screening by Nakshatra Automation.
