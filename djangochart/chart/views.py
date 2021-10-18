from os import name
from django.db.models.fields import IntegerField
from django.shortcuts import render
import json
from django.http import HttpResponse, response
from .models import base
import requests
# Create your views here.
def index(request):
    url=('https://api.openweathermap.org/data/2.5/weather?q={}&appid=60eadf0b6c54c2583131f8a0fd769539')
    city='chennai'  
    res=requests.get(url.format(city)).json()
    city_weather={
        'city':res['name'],
        'temperature':res['main']['temp'],
        'timestamp':res['dt'],
        }
    
    base1=base(
        City=city_weather['city'],
        Temperature=city_weather['temperature'],
        Timestamp=city_weather['timestamp']
    )
    base1.save()
    return render(request,'basic.html')
    