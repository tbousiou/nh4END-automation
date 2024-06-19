from multiprocessing.spawn import import_main_path
from tb_device_mqtt import TBDeviceMqttClient, TBPublishInfo
import random
import time


while True:

    value = random.uniform(0.4, 0.5)

    telemetry = {"ch4": value}
    client = TBDeviceMqttClient('egke.agro.auth.gr', "1LSMLoo9sLyoU1R7j5pS")
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


    value = random.uniform(1800, 1900)

    telemetry = {"nh4": value}
    client = TBDeviceMqttClient('egke.agro.auth.gr', "AvBVBsRnupt46VrfygSh")
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


    value = random.uniform(0.6, 0.65)

    telemetry = {"ch4_prediction": value}
    client = TBDeviceMqttClient('egke.agro.auth.gr', "1LSMLoo9sLyoU1R7j5pS")
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

    time.sleep(5)