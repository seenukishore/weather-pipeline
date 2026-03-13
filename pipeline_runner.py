from extract import extract_weather
from transform import transform_weather
from load import load_weather

cities = ["Chennai", "Mumbai", "Delhi", "Bangalore", "Kolkata"]


def run_pipeline():
    print("\n🌤️ Weather Data Pipeline Started...")
    print("=" * 40)

    for city in cities:
        print(f"\n📍 Processing {city}...")

        # Extract
        raw_data = extract_weather(city)
        if raw_data is None:
            continue

        # Transform
        transformed_data = transform_weather(raw_data)

        # Load
        load_weather(transformed_data)

    print("\n" + "=" * 40)
    print("✅ Weather Pipeline Completed Successfully!")


if __name__ == "__main__":
    run_pipeline()