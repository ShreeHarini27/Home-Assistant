import paho.mqtt.client as mqtt
import time
import random

# ⚠️ CHANGE THESE 3 LINES - PUT YOUR INFO!
student_name = "SHREE HARINI A"
unique_id = "42111225"
topic = "home/shreeharini-2025/sensor"

MQTT_BROKER = "localhost"
MQTT_PORT = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ CONNECTED!")
        print(f"📛 Student: {student_name}")
        print(f"🆔 Register: {unique_id}")
        print(f"📡 Topic: {topic}")

client = mqtt.Client(client_id=f"sensor_{unique_id}")
client.on_connect = on_connect
client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_start()

print("\n🚀 Publishing sensor data...\n")

try:
    count = 1
    while True:
        temperature = 25
        humidity = 60
        light_intensity = random.randint(100, 1000)
        
        client.publish(f"{topic}/temperature", temperature, qos=1)
        client.publish(f"{topic}/humidity", humidity, qos=1)
        client.publish(f"{topic}/light", light_intensity, qos=1)
        
        print(f"[{count}] 🌡️ {temperature}°C | 💧 {humidity}% | 💡 {light_intensity} lux")
        count += 1
        time.sleep(3)
        
except KeyboardInterrupt:
    print("\n⛔ Stopped!")
    client.loop_stop()
    client.disconnect()