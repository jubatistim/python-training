import pyowm

owm = pyowm.OWM('e52968e0024d9e1968a04ba2cd9ac45e')

location = owm.weather_at_place('São Paulo')
weather = location.get_weather()

temp = weather.get_temperature('celsius')

print(temp)