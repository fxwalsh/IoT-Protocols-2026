# Assignment Requirements

Each person/team must **propose, design, and implement** an **IoT-based solution** that includes:

| Requirement                              | Description                                                  | Weight  |
| ---------------------------------------- | ------------------------------------------------------------ | ------- |
| **IoT Device Connection**                | - Set up a **Raspberry Pi 4 or similar device** connected to an **IoT messaging platform or server**. - Configure **MQTT communication or HTTP-based messaging**. - Verify **data transmission from the device to the platform/server**. | **10%** |
| **Sensor Data Collection**               | - Choose **at least two sensors** for monitoring (e.g., temperature, motion, light, etc.). - Write a **Python script** to collect **real-time data** and store it locally. - Ensure the **data is timestamped**. | **15%** |
| **Telemetry Transmission**               | - Format sensor readings as **JSON**. - Implement **secure data transmission using MQTT or HTTP** to the IoT server/platform. - Apply **error handling and retry mechanisms**. | **15%** |
| **Data Visualisation**                   | - Use a **dashboard or visualisation tool** (e.g., IoT dashboard/ web interface) to display sensor trends. - Display key parameters (e.g., **Heart Rate, motion activity**). - Ensure **real-time updates** are reflected on the dashboard. | **15%** |
| **Data Processing & Actuation**          | - Implement an **automated response based on sensor readings**. - Use a **server-side script or event-processing system** to analyse incoming data and trigger actions (e.g., turning on a fan, sending an alert). - If applicable, integrate **computer vision or AI-based analysis** for real-time decision-making. | **30%** |
| **Project Presentation & Documentation** | Submit a **report** that includes: - **System architecture diagrams**. - **Code snippets and explanations**. - **Screenshots of dashboards and telemetry data**. - **Challenges encountered and solutions implemented**. - A **5-minute demonstration video** showcasing the project. | **15%** |