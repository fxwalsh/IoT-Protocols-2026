from azure.storage.blob import ContainerClient
import pandas as pd
import matplotlib.pyplot as plt
import json
import base64

# === Azure Blob Storage setup ===
connect_str = "DefaultEndpointsProtocol=https;AccountName=smsfxwlash;AccountKey=jGZFRcj37LZcJw4NjOyokppIDVLBmCyz7Ey/tAiCEhTviVpx6my7IhefTNsqa5PGLEP+KYduJF0G+ASt1GVLdQ==;EndpointSuffix=core.windows.net"
container_name = "env-data"

client = ContainerClient.from_connection_string(connect_str, container_name)

records = []

for blob in client.list_blobs():
    blob_data = client.download_blob(blob).readall()
    lines = blob_data.decode('utf-8').splitlines()
    
    for line in lines:
        try:
            message = json.loads(line)
            body_b64 = message.get("Body")
            if body_b64:
                body_json = json.loads(base64.b64decode(body_b64).decode('utf-8'))
                timestamp = body_json.get("timestamp", message.get("EnqueuedTimeUtc"))
                records.append({
                    "timestamp": pd.to_datetime(timestamp),
                    "temperature": body_json.get("temperature")
                })
        except Exception as e:
            print(f"Skipped a line in {blob.name}: {e}")

# Create DataFrame
df = pd.DataFrame(records)

if df.empty:
    print("No data parsed!")
else:
    df.sort_values("timestamp", inplace=True)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.plot(df["timestamp"], df["temperature"], marker="o")
    plt.xlabel("Time")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Over Time")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
