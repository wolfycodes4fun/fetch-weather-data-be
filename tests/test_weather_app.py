from src.app import app

def test_get_weather_data_response():
    
    with app.test_client() as client:
        response = client.get('/yourweather/api/v1/fetchcity/London')
        assert response.status_code == 200
        data = response.get_json()
        assert "main" in data
        assert "feels_like" in data["main"]
        assert "humidity" in data["main"]
        assert "wind" in data
        assert "speed" in data["wind"]

def test_get_comfort_index_response():
    with app.test_client() as client:
        response = client.get('/yourweather/api/v1/comfortindex/London')
        assert response.status_code == 200
        data = response.get_json()
        assert "comfort_index" in data
        assert isinstance(data["comfort_index"], float)