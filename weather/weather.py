import pyowm

from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)

import os

SECRET_KEY = os.getenv("OWM_API_KEY")

owm = pyowm.OWM(SECRET_KEY)

location = owm.weather_at_place('São Paulo')
weather = location.get_weather()

temp = weather.get_temperature('celsius')

print(temp)