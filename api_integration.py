import requests

# API Key dhe URL për OpenWeatherMap
api_key = "your_api_key_here"
city = "Tirana"  # Ndryshoni në bazë të nevojave
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# Kërkesa për të marrë të dhënat
response = requests.get(url)
weather_data = response.json()

# Ruajtja e të dhënave në një skedar JSON
import json
with open('weather_data.json', 'w') as file:
    json.dump(weather_data, file)