import requests


def get_weather_data(city):
    geocode_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid=YOUR_API_KEY"
    geocode_response = requests.get(geocode_url).json()

    if not geocode_response:
        return None

    lat = geocode_response[0]['lat']
    lon = geocode_response[0]['lon']

    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid=YOUR_API_KEY"
    weather_response = requests.get(weather_url).json()

    return weather_response
