import json
# import os
from datetime import datetime
import requests

api_key = 'd2f51d8e90cc358457b28c9057605ee5'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')

text_file = open("weather.txt", "a")
text_file.write("-------------------------------------------------------------\n")
text_file.write("Weather Stats for - {}  || {} \n".format(location.upper(), date_time))
text_file.write("-------------------------------------------------------------\n")
text_file.write("Current temperature is: {:.2f} deg C \n".format(temp_city))
text_file.write("Current weather desc  : {} \n".format(weather_desc))
text_file.write("Current Humidity  :   {} % \n".format(hmdt))
text_file.close()
