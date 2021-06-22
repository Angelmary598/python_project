import requests
from datetime import datetime

api_key = '57f8044049657a870154dc6a5af4b416'
print("\b       WEATHER FORECAST\n")
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+api_key
try:
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()

    
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
    print("Current wind speed    :", wind_spd, 'kmph')

    f = open('weather_info.txt', 'w+')
    f.write("Weather Details\n\n")
    f.write(f"Date: {str(date_time)}\n")
    f.write(f"Location: {str(location)}\n")
    f.write(f"Temperature: {round(float(str(temp_city)),2)} deg C\n")
    f.write(f"Weather desc{str(weather_desc)}\n")
    f.write(f"Humidity: {str(hmdt)} %\n")
    f.write(f"Wind speed: {str(wind_spd)} Kmph\n")
    f.close()
    print("\n Weather information is stored in weather_info.txt")
except:
    print("Enter a valid Location")