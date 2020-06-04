from urllib.request import urlopen
import json

# Info to parse
api_key = "f57f78b88df782edef2d267985a11166"  # insert your own API key!!!
zone = "Barcelona,es"
units = "metric"

# Query to URL
response = urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&units={}&appid={}'.format(
    zone, units, api_key)).read()

# Convert to Python DS
data = json.loads(response)  # json.loads() convert the info into a data structure which python understands

##############################################################################################

city = data["name"]
country = data["sys"]["country"]
temperature = data["main"]["temp"]
sensation = data["main"]["feels_like"]

weather_message = """
    City: {}
    Country: {}
    Temp: {}
    Feels like: {}
    
""".format(city, country, temperature, sensation)

# Show weather info
print(weather_message)
