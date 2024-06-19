#!/usr/bin/env python3

# import automationhat
import os
import time
import sys
import paho.mqtt.client as mqtt
import json

from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv('HOST')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

time.sleep(0.1) # short pause after ads1015 class creation recommended
sensor_data = {'temperature': 0}
# automationhat.enable_auto_lights(False)

client = mqtt.Client()
templist = []

# Set access token
client.username_pw_set(ACCESS_TOKEN)

# Connect to ThingsBoard using default MQTT port and 60 seconds keepalive interval
client.connect(HOST, 1883, 60)

client.loop_start()

for x in range(0, 10):
    #value = automationhat.analog.one.read()
    value = 0.5;
    volts = (value)
    temperature = (volts / (10.0 / 1000))-1.5
    # print(u"Temperature: {:g}\u00b0C, Humidity: {:g}%".format(temperature, humidity))
    time.sleep(0.2)
    # next_item = round(random.uniform(2.00, 10.00), 2)
    next_item = (volts / (10.0 / 1000))-1.5
    print(next_item)
    templist.append(next_item)
    print(len(templist))
    if len(templist) >= 10:
        print(templist[4:10])
        avg = sum(templist[4:10]) / len(templist[4:10])
        print(avg)
        formatted = '{0:.4g}'.format(avg)
        print(formatted)
        if avg < 0 and avg >50:
            exit
        sensor_data['temperature'] = formatted
        print("Formated",formatted)

    # Sending temperature data to ThingsBoard
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
        
    
templist = []

client.loop_stop()
client.disconnect()
print("Exit")