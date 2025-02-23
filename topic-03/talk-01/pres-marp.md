---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# IoT in Agriculture

---

## Digital Agriculture

*   Digital agriculture uses tools to collect, store, and analyse farming data  .
*   It is also known as the 'Fourth Agricultural Revolution' or 'Agriculture 4.0'  .
*   It encompasses the entire 'agriculture value chain', from farm to table . This includes tracking produce quality, warehouse systems, and even tractor rental apps .
*   Digital agriculture allows farmers to increase yields, use less fertilizers and pesticides, and optimise water use .
*   'Precision Agriculture' is a technique that observes, measures, and responds to crops on a per-field basis .

---

## Techniques Enabled by Digital Agriculture

*   **Temperature measurement** - to predict plant growth and maturity .
*   **Automated watering** - using soil moisture sensors to water only when needed .
*   **Pest control** - using cameras on robots or drones to apply pesticides only where needed .

---

## Why is Temperature Important?

* Plants need warmth to grow .

* Plants have a **base temperature**, **optimal temperature**, and **maximum temperature** .

* **Base temperature**: the minimum daily average temperature for growth .

* **Optimal temperature**: the best daily average temperature for the most growth .

* **Maximum temperature**: the maximum temperature a plant can withstand, after which growth stops .

* These are average temperatures, averaged over the daily and nightly temperatures .

* Each species of plant has different values for their base, optimal, and maximum .

  ![plant-growth-temp-graph.png](./img/pres-marp/plant-growth-temp-graph.png)

---

## Growing Degree Days (GDD)

*   Growing degree days (GDD) measure plant growth based on temperature .
*   GDD is calculated as the average daily temperature above the plant's base temperature .
*  Each plant needs a specific number of GDD to grow, flower, and mature .
*   A simplified equation to calculate GDD is:

    **GDD = ((Tmax + Tmin) / 2) - Tbase**
    where:
    
    *   Tmax = daily maximum temperature  
    *   Tmin = daily minimum temperature  
    *   Tbase = plant's base temperature  

---

## Calculating GDD with Temperature Sensor Data

*   Farmers can use GDD to estimate when crops will be ready for harvest, instead of relying on fixed dates .
*   IoT devices can measure temperature and publish the data over the Internet using a protocol like MQTT .
*   Server code can listen to this data and save it to a database or file .
*   The data can be analysed later, such as in a nightly job to calculate GDD for each crop and alert the farmer .
*   The server code can also add extra information, such as the location of the device and what crops it's monitoring .

---

## Storing Temperature Data

*   Temperature data can be stored in a CSV file with two columns: date and temperature .
*   The date column shows the date and time the message was received by the server .
*   The temperature column shows the temperature from the IoT device .
*   Each row contains the date/time and the corresponding temperature measurement .

---

## Example: Calculating GDD for Strawberries

*   Base temperature for strawberries: 10°C  
*   Highest daily temperature: 25°C  
*   Lowest daily temperature: 12°C  
*   GDD Calculation:

    ((25 + 12) / 2) - 10 = 8.5 GDD

*   Strawberries need about 250 GDD to bear fruit .

---

## Challenge

*   Plants need more than just heat to grow, such as water, carbon dioxide, and nutrients [1, 17].
*   Sensors can measure these factors and actuators can control them .
*   IoT devices can be used to optimise plant growth by monitoring and controlling these variables .

---

## Review & Self Study

*   Read more on digital agriculture and precision agriculture on Wikipedia .
*   Learn about the full growing degree days calculation on the Growing Degree Day Wikipedia page .
*   Explore hi-tech farming techniques .

---

