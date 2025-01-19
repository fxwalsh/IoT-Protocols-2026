import os
import time
import json
import logging
import schedule
import paho.mqtt.client as mqtt
from urllib.parse import urlparse

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    logging.info("Connection Result: " + str(rc))

def on_publish(client, obj, mid):
    logging.info("Message ID: " + str(mid))



mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish



try:
    mqttc.connect("broker.emqx.io", 1883)
    mqttc.loop_start()
except Exception as e:
    logging.error("Connection failed: " + str(e))
    exit(1)

# Scheduled task for publishing temperature
def publish_temperature():
    temp_json = json.dumps({"deviceID": "RPi1", "temperature": 23.4, "timestamp": time.time()})
    mqttc.publish("fxwalsh/temperature", temp_json, retain=False)

# Schedule the task every 10 seconds
schedule.every(10).seconds.do(publish_temperature)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    logging.info("Script termination requested, shutting down.")
finally:
    mqttc.loop_stop()
    mqttc.disconnect()
