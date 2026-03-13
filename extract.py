import requests

API_KEY = "2ba101d18340f4f5827e9982354575f8"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def extract_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        print(f"✅ Extracted weather data for {city}")
        return data
    else:
        print(f"❌ Error: {data['message']}")
        return None