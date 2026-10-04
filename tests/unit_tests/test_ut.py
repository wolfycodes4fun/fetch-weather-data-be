import os

from src.helper_func import fetch_city_coordinates

OPEN_WEATHER_MAP_API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")

def test_fetch_city_coordinates(mocker):
    # Intercept network calls made in app
    mock_get = mocker.patch('src.helper_func.requests.get')

    # Define fake data the mock should return
    mock_get.return_value.json.return_value = [{"lat": 6.6639728, "lon": 79.9305102}]

    # Call the function
    latitude, longitude = fetch_city_coordinates("Wadduwa", OPEN_WEATHER_MAP_API_KEY)

    assert latitude == 6.6639728
    assert longitude == 79.9305102

    # Verify the network call was actually made by the func
    mock_get.assert_called_once()
