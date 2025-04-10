import requests
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your actual token and datastream
BLYNK_TOKEN = 'thh993Cy_RteNrULPk9Xa_MdXOSBm9IE'
VIRTUAL_PIN = 'v0'
BASE_URL = f'https://fra1.blynk.cloud/external/api/data/get?token={BLYNK_TOKEN}&period=MONTH&granularityType=MINUTE&sourceType=AVG&tzName=America/New_York&format=ISO_SIMPLE&sendEvents=true&dataStreamId=0'

# Get data from Blynk (returns a list of dicts with 'value' and 'createdAt')
response = requests.get(BASE_URL)
if response.ok:
    data = response.json()
    # Convert to DataFrame
    df = pd.DataFrame(data)
    # Convert timestamps to datetime
    df['createdAt'] = pd.to_datetime(df['createdAt'])
    df['value'] = pd.to_numeric(df['value'], errors='coerce')  # convert values to float
    df = df.dropna()

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(df['createdAt'], df['value'])
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(f'Blynk Data from {VIRTUAL_PIN.upper()}')
    plt.grid(True)
    plt.show()
else:
    print('Failed to fetch data:', response.status_code, response.text)
