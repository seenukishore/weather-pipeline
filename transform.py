def transform_weather(data):
    transformed = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "weather_description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }

    print(f"✅ Transformed weather data for {transformed['city']}")
    return transformed