import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        print("\n========== WEATHER REPORT ==========")
        print("City       :", data["name"])
        print("Country    :", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like :", data["main"]["feels_like"], "°C")
        print("Humidity   :", data["main"]["humidity"], "%")
        print("Weather    :", data["weather"][0]["description"].title())
        print("Wind Speed :", data["wind"]["speed"], "m/s")
        print("====================================")

    elif response.status_code == 401:
        print("\nInvalid API key or API key is not active yet.")

    elif response.status_code == 404:
        print("\nCity not found. Please enter a valid city name.")

    else:
        print("\nUnable to fetch weather information.")
        print("Error code:", response.status_code)


print("====================================")
print("       OPENWEATHER WEATHER APP")
print("====================================")

if not API_KEY:
    print("API key is not set.")
else:
    city = input("Enter city name: ")

    if city.strip() == "":
        print("Please enter a city name.")
    else:
        get_weather(city)