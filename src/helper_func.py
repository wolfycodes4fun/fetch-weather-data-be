import requests

def fetch_city_coordinates(city_name, api_key):
    """Fetches latitude & longitude for a given city using the OpenWeatherMap API
    Args:
        city_name (str): The name of the city for which to fetch coordinates.
        api_key (str): The API key for accessing the OpenWeatherMap API.
    Returns:
        tuple: A tuple containing the latitude and longitude of the specified city.
    """
    open_weather_map_geocoding_api_endpoint = "http://api.openweathermap.org/geo/1.0/direct"
    geocoding_endpoint_params = {
        "q": city_name,
        "limit": 1,
        "appid": api_key
    }
    response = requests.get(
        f"{open_weather_map_geocoding_api_endpoint}",
        params=geocoding_endpoint_params,
        timeout=10
    )

    # Decode the JSON response
    response_data = response.json()
    latitude, longitude = response_data[0]["lat"], response_data[0]["lon"]

    return latitude, longitude

def calculate_comfort_index(temperature, humidity, wind_speed):
    """Calculates the comfort index for a given set of weather conditions.
    Args:
        temperature (float): The temperature in Kelvin.
        humidity (float): The humidity as a percentage.
        wind_speed (float): The wind speed in m/s.
    Returns:
        float: The calculated comfort index.
    """
    s_temperature, s_humidity, s_wind_speed = None, None, None

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
