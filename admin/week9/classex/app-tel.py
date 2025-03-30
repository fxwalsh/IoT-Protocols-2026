import json
from sqlite3.dbapi2 import Timestamp
import time
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import json
import random
from datetime import datetime  
connection_string = "HostName=soil-moisture-sensor-fxwalsh.azure-devices.net;DeviceId=env-sensor;SharedAccessKey=PqAYHo7GYD1HDL/sblfAnLm4gzBBHG/wrY7RaGAY5qU="
def get_env_data():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "temperature": round(random.uniform(15.0, 30.0), 2),  # Celsius
        "humidity": round(random.uniform(30.0, 80.0), 2),     # Percent
        "pressure": round(random.uniform(980.0, 1050.0), 2)   # hPa
    }

device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

print('Connecting')
device_client.connect()
print('Connected')


    
while True:

    
    line = get_env_data()         
    print(line)  # Print the data dictionary
    message = Message(json.dumps(line))
    device_client.send_message(message)
    time.sleep(1)