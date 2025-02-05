---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# Predicting Plant Growth with IoT

---

## Digital Agriculture

*   Digital agriculture uses tools to collect, store, and analyse farming data [1].
*   It is also known as the 'Fourth Agricultural Revolution' or 'Agriculture 4.0' [1].
*   It encompasses the entire 'agriculture value chain', from farm to table [2]. This includes tracking produce quality, warehouse systems, and even tractor rental apps [2].
*   Digital agriculture allows farmers to increase yields, use less fertilizers and pesticides, and optimise water use [2].
*   'Precision Agriculture' is a technique that observes, measures, and responds to crops on a per-field basis [3].

---

## Techniques Enabled by Digital Agriculture

*   **Temperature measurement** - to predict plant growth and maturity [4].
*   **Automated watering** - using soil moisture sensors to water only when needed [4].
*   **Pest control** - using cameras on robots or drones to apply pesticides only where needed [4].

---

## Why is Temperature Important?

*   Plants need warmth to grow [3].
*   Plants have a **base temperature**, **optimal temperature**, and **maximum temperature** [5].
*   **Base temperature**: the minimum daily average temperature for growth [5].
*   **Optimal temperature**: the best daily average temperature for the most growth [5].
*  **Maximum temperature**: the maximum temperature a plant can withstand, after which growth stops [5].
*   These are average temperatures, averaged over the daily and nightly temperatures [6].
*   Each species of plant has different values for their base, optimal, and maximum [6].

---

## Measuring Ambient Temperature

*   Temperature sensors can be used with IoT devices to measure ambient temperature [7].
*   You can use guides to monitor temperatures using IoT devices such as:
    *   Arduino - Wio Terminal [7]
    *   Single-board computer - Raspberry Pi [7]
    *   Single-board computer - Virtual device [7]

---

## Growing Degree Days (GDD)

*   Growing degree days (GDD) measure plant growth based on temperature [8].
*   GDD is calculated as the average daily temperature above the plant's base temperature [8].
*  Each plant needs a specific number of GDD to grow, flower, and mature [8].
*   A simplified equation to calculate GDD is:

    **GDD = ((Tmax + Tmin) / 2) - Tbase**
    where:
    *   Tmax = daily maximum temperature [9]
    *   Tmin = daily minimum temperature [9]
    *   Tbase = plant's base temperature [9]

---

## Calculating GDD with Temperature Sensor Data

*   Farmers can use GDD to estimate when crops will be ready for harvest, instead of relying on fixed dates [10].
*   IoT devices can measure temperature and publish the data over the Internet using a protocol like MQTT [11].
*   Server code can listen to this data and save it to a database or file [11].
*   The data can be analysed later, such as in a nightly job to calculate GDD for each crop and alert the farmer [11].
*   The server code can also add extra information, such as the location of the device and what crops it's monitoring [12].

---

## Storing Temperature Data

*   Temperature data can be stored in a CSV file with two columns: date and temperature [13].
*   The date column shows the date and time the message was received by the server [14].
*   The temperature column shows the temperature from the IoT device [14].
*   Each row contains the date/time and the corresponding temperature measurement [15].

---

## Example: Calculating GDD for Strawberries

*   Base temperature for strawberries: 10°C [16]
*   Highest daily temperature: 25°C [16]
*   Lowest daily temperature: 12°C [16]
*   GDD Calculation:

    ((25 + 12) / 2) - 10 = 8.5 GDD [16, 17]

*   Strawberries need about 250 GDD to bear fruit [17].

---

## Challenge

*   Plants need more than just heat to grow, such as water, carbon dioxide, and nutrients [1, 17].
*   Sensors can measure these factors and actuators can control them [17].
*   IoT devices can be used to optimise plant growth by monitoring and controlling these variables [17].

---

## Review & Self Study

*   Read more on digital agriculture and precision agriculture on Wikipedia [17].
*   Learn about the full growing degree days calculation on the Growing Degree Day Wikipedia page [17].
*   Explore hi-tech farming techniques [17].

---

