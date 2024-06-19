import requests, datetime, helpers
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
from dotenv import load_dotenv
import os

load_dotenv()

TENANT_USERNAME = os.getenv('TENANT_USERNAME')
TENANT_PASSWORD = os.getenv('TENANT_PASSWORD')
SERVER = os.getenv('SERVER')

jwt_token = helpers.get_jwt_token(SERVER, TENANT_USERNAME, TENANT_PASSWORD)


headers = {
    'accept': 'application/json',
    'X-Authorization': f"Bearer {jwt_token}",
}

params = (
    ('keys', 'CH4'),
    ('useStrictDataTypes', 'true'),
)
print("geting response")
response = requests.get('http://egke.agro.auth.gr:8080/api/plugins/telemetry/DEVICE/8d2d1b00-8a6b-11ec-97a9-b1b6e0531f07/values/timeseries', headers=headers, params=params)
print("response done")

response_data = response.json()
value = response_data['CH4'][0]['value']

print(response.json())
#print(round(value,2))

telemetry = {"daily_ch4": value}
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
