#!/usr/bin/python3

import logging
import paho.mqtt.client as mqtt
from urllib.parse import urlparse
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Connected successfully")
    else:
        logging.error(f"Connection failed with code {rc}")

def on_message(client, obj, msg):
    logging.info(f"Topic: {msg.topic}, Payload: {msg.payload.decode()}")

def on_subscribe(client, obj, mid, granted_qos):
    logging.info(f"Subscribed: {mid}, QOS granted: {granted_qos}")




mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

try:
    mqttc.connect("broker.emqx.io", 1883)
    mqttc.loop_start()
    # Subscribe or publish messages here as needed
except Exception as e:
    logging.error(f"Connection failed: {e}")
    exit(1)

try:
    
    mqttc.subscribe("fxwalsh/#", qos=0)

    # Keep the script running
    input("Press Enter to exit...\n")
except KeyboardInterrupt:
    pass
finally:
    mqttc.loop_stop()
    mqttc.disconnect()
    logging.info("Disconnected from MQTT broker.")