import os
from flask import Flask
import requests

from helper_func import fetch_city_coordinates, calculate_comfort_index

app = Flask(__name__)

OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
OPEN_WEATHER_MAP_FETCH_WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/yourweather/api/v1/fetchcity/<city>", methods=["GET"])
def fetch_weather_data(city):
    """Fetches weather data for a given city using the OpenWeatherMap API
    Args:
        city (str): The name of the city for which to fetch weather data.
    Returns:
        dict: A JSON object with weather data for the specified city.
    """
    latitude, longitude = fetch_city_coordinates(city, OPEN_WEATHER_MAP_API_KEY)

    fetch_weather_endpoint_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": OPEN_WEATHER_MAP_API_KEY
    }
    response = requests.get(
        f"{OPEN_WEATHER_MAP_FETCH_WEATHER_API_ENDPOINT}",
        params=fetch_weather_endpoint_params,
        timeout=10
    )

    return response.json()

@app.route("/yourweather/api/v1/comfortindex/<city>", methods=["GET"])
def return_comfort_index(city):
    """Fetches weather data for a given city using the OpenWeatherMap API
    Args:
        city (str): The name of the city for which to calculate the comfort index.
    Returns:
        dict: A JSON object with the comfort index for the specified city.
    """
    weather_data = fetch_weather_data(city)

    temperature = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    comfort_index = calculate_comfort_index(temperature, humidity, wind_speed)

    return {"comfort_index": comfort_index}
