# Weather Data Pipeline

## About
A Python-based Weather Data Pipeline that fetches real-time weather data from OpenWeatherMap API, transforms it, and stores it in MySQL database.

## Technologies Used
- Python 3
- OpenWeatherMap API
- MySQL Connector
- Cryptography (Fernet)

## Project Structure
| File | Description |
|------|-------------|
| `pipeline_runner.py` | Main pipeline runner |
| `extract.py` | Fetches weather data from API |
| `transform.py` | Cleans and transforms data |
| `load.py` | Loads data into MySQL |
| `password_utils.py` | Encrypted password handler |
| `.gitignore` | Hides secret.key from GitHub |

## ETL Process
- **Extract** → Real-time weather data from OpenWeatherMap API
- **Transform** → Extract temperature, humidity, wind speed, description
- **Load** → Store into `weather_db.weather_data` MySQL table

## Cities Tracked
- Chennai, Mumbai, Delhi, Bangalore, Kolkata

## Security
- `secret.key` is never uploaded to GitHub
- Password is encrypted using Fernet encryption

## How to Run
1. Clone the repository
2. Install dependencies:
```
   pip install mysql-connector-python requests cryptography
```
3. Get free API key from [openweathermap.org](https://openweathermap.org)
4. Add API key in `extract.py`
5. Run `pipeline_runner.py`