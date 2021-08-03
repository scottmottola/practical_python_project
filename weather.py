import requests

def getWeatherAndTemp():
    api_key = "0fccfc512f80268a389076cd387eb7ad"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=" + api_key + "&units=imperial"

    request = requests.get(url)
    json = request.json()
    # print(json)


    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return{'descritption': description,
    'temp_min': temp_min,
    'temp_max': temp_max}

def main():
    weather_dict = getWeatherAndTemp()
    print("Today's forcast is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The maximum temperature is", weather_dict.get('temp_max'))

main()