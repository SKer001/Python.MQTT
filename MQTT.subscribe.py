import paho.mqtt.client as mqtt
import random
import json
import datetime 
import time
import asyncio


Topic = str(input("Subscribe a topic: "))

local_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

@local_client.connect_callback()
def on_connect(client, userdata, connect_flags, reason_code, propertie):
    print(f"Connected with result code {reason_code}\nconnect_flags: {connect_flags}")
    client.subscribe(Topic)
@local_client.message_callback()
def on_message(client, userdata, message):
    print(message.payload.decode("utf-8"))
    pass

#local_client.on_message = on_message

#local_client.on_connect = on_connect

local_client.connect(host="broker.hivemq.com",port=1883,keepalive=60)


local_client.loop_forever()






