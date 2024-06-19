import requests

def get_jwt_token(server=None, username=None,password=None):
    """ GET JWT TOKEN FROM THINGSBOARD """
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    json_data = {
        'username': username,
        'password': password,
    }
    url = server + '/api/auth/login'
    
    response = requests.post(url, headers=headers, json=json_data)

    jwt_token = response.json()['token']
    return jwt_token

def get_latest_timeseries_key(server,username,password,deviceid,key):
    # Server parameters
    TENANT_USERNAME = username
    TENANT_PASSWORD = password
    SERVER = server

    # Device and key parameters
    DEVICEID = deviceid
    KEY = key

    jwt_token = get_jwt_token(SERVER, TENANT_USERNAME, TENANT_PASSWORD)


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
        return value

    return None


def get_attributes(server,username,password,deviceid,keys):
    jwt_token = get_jwt_token(server, username, password)
    
    headers = {
        'accept': 'application/json',
        'X-Authorization': f"Bearer {jwt_token}",
    }

    params = {
        'keys': keys,
    }

    URL = f"{server}/api/plugins/telemetry/DEVICE/{deviceid}/values/attributes"
    
    response = requests.get(URL, headers=headers, params=params)

    if response.ok:
        response_data = response.json()
        data = {item['key']:item['value'] for item in response_data}
        return data
    return None


def relay_time(reactor_volume,sub_vs,flow_rate,vs):
    return (reactor_volume * sub_vs * 0.01 * vs) / flow_rate