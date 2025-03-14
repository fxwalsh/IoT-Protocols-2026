# 📌 Assignment Requirements

Each persteam must **propose, design, and implement** an IoT-based solution that includes:

| **Requirement**                          | **Description**                                              | **Weight** |
| ---------------------------------------- | ------------------------------------------------------------ | ---------- |
| **IoT Device Connection**                | - Set up a **Raspberry Pi 4**/**Device** with an **Azure IoT Hub**. <br> - Configure **MQTT communication** or **Azure SDK-based messaging**. <br> - Verify **data transmission** | **10%**    |
| **Sensor Data Collection**               | - Choose at least **two sensors** for monitoring _(e.g., temperature, motion, light, etc.)_. <br> - Write a **Python script** to collect **real-time data** and store it **locally**. <br> - Ensure **data is timestamped** | **15%**    |
| **Telemetry Transmission to IoT Hub**    | - Format sensor readings as **JSON**. <br> - Implement **secure data transmission** with **MQTT or HTTP** to Azure IoT Hub. <br> - Apply **error handling** and **retry mechanisms**. | **15%**    |
| **Data Visualisation**                   | - Use **Azure Time Series Insights** or **Power BI** to **visualise sensor trends**. <br> - Display key parameters _(e.g., temperature history, motion activity)_. <br> - Ensure **real-time updates** are reflected on the dashboard. | **15%**    |
| **Data Processing & Actuation**          | - Implement an **automated response** based on sensor readings. <br> - Use **Azure Functions** to **analyse data** and trigger actuations _(e.g., turning on a fan, sending an emergency alert)_. <br> - If applicable, integrate **Custom Vision AI** for real-time decision-making _(e.g., recognising falls, detecting abnormal medication intake)_. | **30%**    |
| **Project Presentation & Documentation** | - Submit a **report** with: <br> - **System architecture diagrams**. <br> - **Code snippets** and explanations. <br> - **Screenshots** of dashboards and telemetry data. <br> - **Challenges faced** and solutions implemented. <br> - Deliver a **5-minute demo video** showcasing the project. | **15%**    |