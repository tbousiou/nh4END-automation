from dotenv import load_dotenv
import os
load_dotenv()

HOST = os.getenv('HOST')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
telemetry = {"test_key": 31.9, "biogas_counter":2740, "ch4_counter":4907}
client = TBDeviceMqttClient(HOST, username=ACCESS_TOKEN)
# Connect to ThingsBoard
client.connect()

exit()
# Sending telemetry without checking the delivery status
#client.send_telemetry(telemetry) 
# Sending telemetry and checking the delivery status (QoS = 1 by default)
result = client.send_telemetry(telemetry)
# get is a blocking call that awaits delivery status  
success = result.get() == TBPublishInfo.TB_ERR_SUCCESS

print(success)
# Disconnect from ThingsBoard
client.disconnect()