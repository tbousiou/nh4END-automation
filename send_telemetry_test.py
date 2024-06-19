from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import random
import time
from timeit import default_timer as timer

from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv('HOST')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

KEY = 'test_send_block'






for i in range(5):
    value = random.uniform(20, 25)

    telemetry = {KEY: value}

    client = TBDeviceMqttClient(HOST, ACCESS_TOKEN)
    # Connect to ThingsBoard
    client.connect()
    # Sending telemetry without checking the delivery status
    # client.send_telemetry(telemetry) 
    # Sending telemetry and checking the delivery status (QoS = 1 by default)
    
    result = client.send_telemetry(telemetry)
    # get is a blocking call that awaits delivery status  
    start = timer()
    success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
    end = timer()
    print(success)
    print(end-start)
    # Disconnect from ThingsBoard
    client.disconnect()
    