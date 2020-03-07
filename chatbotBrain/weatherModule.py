import requests, json 
  
# Enter your API key here 
api_key = "1823d99319968d567f79ffe2c8ddfb4e"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
# Give city name 
# city_name = input("Enter city name : ") 
  

  
def getWeather(cityName):
    city_name = cityName
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url+"&units=metric")
    x = response.json()
    if x["cod"] != "404": 
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
    
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
    
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
    
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
    
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
    
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"]

        cloudyOrNot = "cloudy" if (x["clouds"]["all"] > 15) else "clear"

        visibility = x["visibility"]/1000

        return "It is currently {}°C in {}. It's {} outside and visibility is {} KM.".format(str(current_temperature),cityName,cloudyOrNot,visibility)
    
        # print following values 
        # print(" Temperature (in kelvin unit) = " +
        #                 str(current_temperature) + 
        #     "\n atmospheric pressure (in hPa unit) = " +
        #                 str(current_pressure) +
        #     "\n humidity (in percentage) = " +
        #                 str(current_humidiy) +
        #     "\n description = " +
        #                 str(weather_description)) 
    
    else: 
        return "city not found"