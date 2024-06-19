#import requests, datetime, helpers
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo



telemetry = {"biogas_counter": 93}
client = TBDeviceMqttClient('egke.agro.auth.gr', "xwmFu1s7RTnPnzCnMwHG")
# Connect to ThingsBoard
client.connect()
# Sending telemetry without checking the delivery status
# client.send_telemetry(telemetry) 
# Sending telemetry and checking the delivery status (QoS = 1 by default)
result = client.send_telemetry(telemetry)
# get is a blocking call that awaits delivery status  
success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
# Disconnect from ThingsBoard
print(success)
client.disconnect()