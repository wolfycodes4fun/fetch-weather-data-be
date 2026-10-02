from flask import Flask
import requests
import os

app = Flask(__name__)

OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
OPEN_WEATHER_MAP_GEOCODING_API_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"
OPEN_WEATHER_MAP_FETCH_WEATHER_API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

def fetch_city_coordinates(city_name):
    response = requests.get(f"{OPEN_WEATHER_MAP_GEOCODING_API_ENDPOINT}?q={city_name}&limit=1&appid={OPEN_WEATHER_MAP_API_KEY}")

    # Decode the JSON response
    response_data = response.json()
    latitude, longitude = response_data[0]["lat"], response_data[0]["lon"]

    return latitude, longitude

@app.route("/weather/api/v1/fetchforcity/<city>", methods=["GET"])
def fetch_weather_data(city):
    latitude, longitude = fetch_city_coordinates(city)

    response = requests.get(f"{OPEN_WEATHER_MAP_FETCH_WEATHER_API_ENDPOINT}?lat={latitude}&lon={longitude}&appid={OPEN_WEATHER_MAP_API_KEY}")

    return response.json()

def calculate_comfort_index(temperature, humidity, wind_speed):

    # Calculate sub-score for temperature
    if 294.15 <= temperature <= 308.15:
        s_temperature = 100
    elif temperature >= 308.15:
        s_temperature = max(0, 100 - (temperature - 308.15) * 12.5)
    elif temperature <= 294.15:
        s_temperature = max(0, 100 - (294.15 - temperature) * 9.1)

    # Calculate sub-score for humidity
    if 30 <= humidity <= 50:
        s_humidity = 100
    elif humidity <= 30:
        s_humidity = max(0, 100 - (30 - humidity) * 10)
    elif humidity >= 50:
        s_humidity = max(0, 100 - (humidity - 50) * 10)

    # Calculate sub-score for wind speed
    if 1.67 <= wind_speed <= 3.06:
        s_wind_speed = 100
    elif wind_speed < 1.67:
        s_wind_speed = max(0, 100 - (1.67 - wind_speed) * 59.88)
    elif wind_speed > 3.06:
        s_wind_speed = max(0, 100 - (wind_speed - 3.06) * 27.7)

    # Calculate overall comfort index with weighted metrics
    comfort_index = (0.5 * s_temperature) + (0.35 * s_humidity) + (0.15 * s_wind_speed)
    
    return comfort_index

@app.route("/weather/api/v1/comfortindex/<city>", methods=["GET"])
def return_comfort_index(city):
    weather_data = fetch_weather_data(city)

    temperature = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]

    comfort_index = calculate_comfort_index(temperature, humidity, wind_speed)
    
    return {"comfort_index": comfort_index}
