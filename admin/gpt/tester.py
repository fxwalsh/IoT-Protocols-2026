import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Weather in {city}: {weather}, Temperature: {temperature}°C"
    else:
        return "Error: Unable to fetch weather data."

def main():
    api_key = '56f1951baca7d4d5030b38c28fc962d4'  # Replace with your OpenWeatherMap API key
    city = "Tramore"
    print(get_weather(api_key, city))

if __name__ == "__main__":
    main()
