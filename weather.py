import pyowm

owm = pyowm.OWM('88f5340678957b9b848effa6c8527802')  # You MUST provide a valid API key


# Search for current weather in Milwaukee (United States)
observation = owm.weather_at_place('Milwaukee,US')
w = observation.get_weather()
today = w.get_temperature('fahrenheit')

#print(today)
print("Current Temp in Milwaukee: {0}".format((today.get('temp'))))

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
