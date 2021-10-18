import mysql.connector
from mysql.connector.dbapi import Timestamp
import requests
import time
import datetime
mydb=mysql.connector.connect(host='localhost',user='root',password='root',database='pydb')
mycursor=mydb.cursor()
def weather():
    count=0
    while True:
        outside_source_url='https://api.openweathermap.org/data/2.5/weather?q=chennai&appid=60eadf0b6c54c2583131f8a0fd769539'
        req=requests.get(outside_source_url).json()
        city_weather={
            'cityname':req['name'],
            'temperature':req['main']['temp'],
            'timestamp':req['dt'],
            }
        outside_source_url='https://api.openweathermap.org/data/2.5/weather?q=toronto&appid=60eadf0b6c54c2583131f8a0fd769539'
        request=requests.get(outside_source_url).json()
        city_weather_1={
            'cityname':request['name'],
            'temperature':request['main']['temp'],
            'timestamp':request['dt'],
            }
        local_time=datetime.datetime.now().strftime('%H:%M:%S')
        local_timestamp=datetime.datetime.now().timestamp()
        print(city_weather,city_weather_1,local_time,local_timestamp)
        time.sleep(0.5)
        count+=1

def db_conn():
    city_weather=weather
    tb='CREATE TABLE weatherapp(id int AUTO_INCREMENT PRIMARY KEY,city_name VARCHAR(50),Temperature VARCHAR(50),Timestamp int)'
    tb_insert='INSERT weatherapp VALUES(%s,%s,%s)'
    values=(city_weather['cityname'],city_weather['temperature'],city_weather['Timestamp'])
    mycursor.execute(tb_insert,values)
    mydb.commit()
    
db_conn()
weather()
