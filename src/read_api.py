import os
import json
import requests

def get_weather_data(API_KEY):
    city = "Chicago"
    base_url = "http://api.weatherstack.com/current"
    
    params = {
        "access_key": API_KEY,
        "query": city
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    with open(f"data/weather.json", "w") as f:
        json.dump(data, f)
    
    with open(f"logs/weather_{data.current.localtime}.log", "a") as log_file:
        log_file.write(f"Fetched weather data for {city}\n")
    
    print(data)
    print("Query Complete!")

if __name__ == "__main__":
    get_weather_data(os.getenv("WEATHER_API_KEY"))