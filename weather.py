import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()
def get_current_weather(city = 'London'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == "__main__":
    print("\n*** Current Weather Data ***\n")
    city = input("Enter city name: ")
    if not bool(city.strip()):
        city = 'London'
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    print(f"\nCurrent weather for {weather_data['name']}")
    print(f"Temperature currently at {weather_data['main']['temp']}")
    print(f"Feels like {weather_data['main']['feels_like']} and {weather_data['weather'][0]['description']}")