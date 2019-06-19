from datetime import datetime
from dotenv import load_dotenv
import os
import pytz
import requests
import math

load_dotenv()  # obtain the weather key from .env file

API_KEY = os.getenv("WEATHER_KEY")

API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city + ",US", API_KEY)).json()
        print(data['main']['temp'])
        data['main']['temp'] = data['main']['temp'] * 9.0/5.0 + 32  # Convert celcius to fahrenheit
        print(data['main']['temp'])
    except Exception as exc:
        print(exc)
        data = None
    return data