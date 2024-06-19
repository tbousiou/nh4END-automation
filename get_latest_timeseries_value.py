import requests, helpers

from dotenv import load_dotenv
import os

load_dotenv()

TENANT_USERNAME = os.getenv('TENANT_USERNAME')
TENANT_PASSWORD = os.getenv('TENANT_PASSWORD')
SERVER = os.getenv('SERVER')

# Device and key parameters
DEVICEID = '36fcba00-8d82-11ec-97a9-b1b6e0531f07'
KEY = 'ch4_counter'

jwt_token = helpers.get_jwt_token(SERVER, TENANT_USERNAME, TENANT_PASSWORD)


headers = {
    'accept': 'application/json',
    'X-Authorization': f"Bearer {jwt_token}",
}

params = (
    ('keys', KEY),
    ('useStrictDataTypes', 'true'),
)

URL = f"{SERVER}/api/plugins/telemetry/DEVICE/{DEVICEID}/values/timeseries"
print(URL)
response = requests.get(URL, headers=headers, params=params)

if response:
    print("Response OK")
    response_data = response.json()
    print(response_data)
    
    value = response_data[KEY][0]['value']
    if value is None:
        print("Value not found, init to zero")
        value = 0

else:
    print("Response failed")
    value = 0




