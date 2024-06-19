import requests, datetime, helpers
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo

from dotenv import load_dotenv
import os

load_dotenv()

TENANT_USERNAME = os.getenv('TENANT_USERNAME')
TENANT_PASSWORD = os.getenv('TENANT_PASSWORD')
SERVER = os.getenv('SERVER')

jwt_token = helpers.get_jwt_token(SERVER, TENANT_USERNAME, TENANT_PASSWORD)


today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)

startTs = int(yesterday.timestamp() * 1000)
endTs = int(today.timestamp() * 1000)

headers = {
    'accept': 'application/json',
    'X-Authorization': f"Bearer {jwt_token}",
}

params = (
    ('keys', 'nh4'),
    ('startTs', startTs),
    ('endTs', endTs),
    ('interval', 86400000),
    ('agg', 'AVG'),
    ('useStrictDataTypes', 'true'),
)
print("geting response")
response = requests.get('http://egke.agro.auth.gr:8080/api/plugins/telemetry/DEVICE/12992ff0-899e-11ec-97a9-b1b6e0531f07/values/timeseries', headers=headers, params=params)
print("response done")
# nh4_data = response.json()['nh4']
# print(len(nh4_data))
# for item in nh4_data:
#     ts = item['ts']
#     #print(ts)
#     #dt = datetime.datetime.fromtimestamp(float(ts))
#     d = datetime.datetime.fromtimestamp(ts/1000)
#    print(d)
response_data = response.json()
value = response_data['nh4'][0]['value']

print(response.json())
print(round(value,2))

telemetry = {"daily_nh4": round(value,2)}
client = TBDeviceMqttClient('egke.agro.auth.gr', "xwmFu1s7RTnPnzCnMwHG")
# Connect to ThingsBoard
client.connect()
# Sending telemetry without checking the delivery status
# client.send_telemetry(telemetry) 
# Sending telemetry and checking the delivery status (QoS = 1 by default)
result = client.send_telemetry(telemetry)
# get is a blocking call that awaits delivery status  
success = result.get() == TBPublishInfo.TB_ERR_SUCCESS
print(success)
# Disconnect from ThingsBoard
client.disconnect()