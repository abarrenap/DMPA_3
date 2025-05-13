
import json
import numpy as np
from datetime import datetime
import time
import paho.mqtt.client as mqtt
import os
json_file = 'data/tweets1.json'

# MQTT broker-aren konfigurazioa
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = "txioak"

# MQTT bezeroa sortu eta konektatu
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

gap = 4
with open(json_file, 'r') as file:
    tweets = json.load(file)
    while True:
        try:
            user = np.random.randint(len(tweets))
            tweet = np.random.randint(len(tweets[user]["tweets"]))
            # Produce the JSON data to the Kafka topic
            now = datetime.now()
            formatted = now.strftime("%Y-%m-%d %H:%M:%S")
            text = tweets[user]["tweets"][tweet].encode('utf-8','ignore').decode("utf-8").replace('\n', ' ')
            text += "."
            text = text.replace('"', "")
            text = text.replace('\\', "")
            # tweets[user]["tweets"][tweet].encode("utf-8").decode('utf-8','ignore')
            payload = json.dumps({
            "user_id": str(tweets[user]["id"]),
            "text": text,
            "timestamp": formatted
            })

            result = client.publish(MQTT_TOPIC, payload)
    
            status = result[0]
            if status == 0:
                print(f"✅ Bidalia: {payload}")
            else:
                print(f"❌ Ezin izan da bidali: {payload}")
            time.sleep(2)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            # Introduce a delay between insertions
            time.sleep(gap)
print("huehue")

    # print("Flights", line.to_json()[:-1] + ', "time": ' + str(time.time()) + "}")
