import requests
import pandas as pd
from datetime import datetime
import gzip

api_key = "f395e40ca27746b915d53030398e8357"

cities = ["Moscow", "Krasnodar", "Novosibirsk", "Yekaterinburg", "Kazan"]


def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather_data = {
        "city": city,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
    }
    return weather_data


all_weather_data = []
for city in cities:
    weather_data = get_weather_data(city)
    all_weather_data.append(weather_data)

df = pd.DataFrame(all_weather_data)

filename = "weather_data.csv.gz"
with gzip.open(filename, "wt", encoding="utf-8") as f:
    df.to_csv(f, index=False)
