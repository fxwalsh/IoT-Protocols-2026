import json
from sqlite3.dbapi2 import Timestamp
import time
from azure.iot.device import IoTHubDeviceClient, Message, MethodResponse
import json
import os
import uuid
from azure.storage.blob import BlobServiceClient
from datetime import datetime  
connection_string = "HostName=soil-moisture-sensor-fxwalsh.azure-devices.net;DeviceId=env-sensor;SharedAccessKey=PqAYHo7GYD1HDL/sblfAnLm4gzBBHG/wrY7RaGAY5qU="
def get_env_data():
    # Corrected the dictionary keys to be strings
    data = {"temperature": 0, "humidity": 0, "pressure": 0}
    return data  # Ensure the function returns the data dictionary

device_client = IoTHubDeviceClient.create_from_connection_string(connection_string)

print('Connecting')
device_client.connect()
print('Connected')

device_id = os.getenv('IOTEDGE_DEVICEID', 'env-sensor')

def get_or_create_container(name):
    connection_str = "DefaultEndpointsProtocol=https;AccountName=smsfxwlash;AccountKey=jGZFRcj37LZcJw4NjOyokppIDVLBmCyz7Ey/tAiCEhTviVpx6my7IhefTNsqa5PGLEP+KYduJF0G+ASt1GVLdQ==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_str)

    for container in blob_service_client.list_containers():
        if container.name == name:
            return blob_service_client.get_container_client(container.name)
    
    return blob_service_client.create_container(name)
    
while True:

    blob_name = f'{device_id}/{str(uuid.uuid1())}.json'
    container_client = get_or_create_container('env-data')
    blob = container_client.get_blob_client(blob_name)
    
    line = get_env_data()         
    print(line)  # Print the data dictionary
    message = Message(json.dumps(line))
    blob_body = {
    'device_id' : device_id,
    'timestamp' : datetime.now().isoformat(),
    'data': line
    }
    print(blob_body)
    blob.upload_blob(json.dumps(blob_body).encode('utf-8'))
    device_client.send_message(message)
            
    

    time.sleep(1)