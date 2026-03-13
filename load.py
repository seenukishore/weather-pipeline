import mysql.connector
from password_utils import get_decrypted_password


def load_weather(data):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=get_decrypted_password(),
        database="weather_db"
    )
    cursor = conn.cursor()

    cursor.execute("""
                   INSERT INTO weather_data
                   (city, temperature, feels_like, humidity, weather_description, wind_speed)
                   VALUES (%s, %s, %s, %s, %s, %s)
                   """, (
                       data["city"],
                       data["temperature"],
                       data["feels_like"],
                       data["humidity"],
                       data["weather_description"],
                       data["wind_speed"]
                   ))

    conn.commit()
    conn.close()
    print(f"✅ Loaded weather data for {data['city']} into MySQL")