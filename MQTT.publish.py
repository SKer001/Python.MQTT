import paho.mqtt.client as mqtt
import random
import json
import datetime 
import time
import asyncio

local_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

Topic = "hhhh"

def on_connect(client, userdata, connect_flags, reason_code, propertie):
    print(f"Connected with result code {reason_code}\nconnect_flags: {connect_flags}")
    client.subscribe(Topic)

def publish_data():
    Temperature = random.randint(0,30) #隨機數0~30
    Time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") #年-月-日-時-分-秒
    payload = {'Temperature' : Temperature , 'Time' : Time}
    print (json.dumps(payload))#要發布的主題和內容
    local_client.publish(Topic, json.dumps(payload))
    time.sleep(5)
    pass

local_client.connect(host="broker.hivemq.com",port=1883,keepalive=60)

local_client.on_connect = on_connect

while True:
    publish_data()