import requests


location=input('enter the location')
outside_source_url='https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid=60eadf0b6c54c2583131f8a0fd769539'
req=requests.get(outside_source_url).json()
city_weather={
    'cityname':req['city'],
    'temperature':req['main']['temp'],
    'timstamp':req['dt']
}
print(city_weather)