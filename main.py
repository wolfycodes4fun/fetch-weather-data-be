from flask import Flask
import requests
import os

app = Flask(__name__)

OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
OPEN_WEATHER_MAP_GEOCODING_API_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"
OPEN_WEATHER_MAP_FETCH_WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

def fetch_city_coordinates(city_name):
    response = requests.get(f"{OPEN_WEATHER_MAP_GEOCODING_API_ENDPOINT}?q={city_name}&limit=1&appid={OPEN_WEATHER_MAP_API_KEY}")

    # Decode the JSON response
    response_data = response.json()
    latitude, longitude = response_data[0]["lat"], response_data[0]["lon"]

    print(f"Fetched coordinates for city '{city_name}': Latitude = {latitude}, Longitude = {longitude}")
    return latitude, longitude

@app.route("/weather/api/v1/fetchforcity/<city>", methods=["GET"])
def fetch_weather_data(city):
    latitude, longitude = fetch_city_coordinates(city)

    response = requests.get(f"{OPEN_WEATHER_MAP_FETCH_WEATHER_API_ENDPOINT}?lat={latitude}&lon={longitude}&appid={OPEN_WEATHER_MAP_API_KEY}")

    return response.json()

def calculate_comfort_index(temperature, humidity, wind_speed, cloudiness, pressure, visibility):
    pass
