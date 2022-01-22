from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from .models import City_wheather
from .forcast_model import forcast


def get_weather(request):
    key = "d094ea8e2b504d63b38174904210512"
    city = "Москва"
    if request.method == 'POST':
        city = request.POST['city']
    today_city_info = get_whether_today(key, city)
    tomorrow_city_info = get_whether_tomorrow(key, city)
    previous_7days = get_previous_7days(key, city)
    model_info = forcast(tomorrow_city_info['temp'],today_city_info['temp'],previous_7days)
    if request.method == 'POST':
        update_or_create(city,tomorrow_city_info['temp'],today_city_info['temp'],previous_7days)
    context = {'today_city_info': today_city_info,
               'tomorrow_city_info': tomorrow_city_info
               }
    print(model_info)
    return render(request, 'weather/get_weather.html', context)


def get_whether_today(key, city):
    url = "https://api.weatherapi.com/v1/current.json?key={0}&q={1}&aqi=no&lang=ru"
    res = requests.get(url.format(key, city)).json()
    city_info = {
        'city': city,
        'temp': res["current"]["temp_c"],
        'icon_text': res["current"]["condition"]["text"],
        'icon': res["current"]["condition"]["icon"],
    }
    return city_info


def get_whether_tomorrow(key, city):
    url = "https://api.weatherapi.com/v1/forecast.json?key={0}&q={1}&days=1&aqi=no&alerts=no&lang=ru"
    res = requests.get(url.format(key, city)).json()
    city_info = {
        'city': city,
        'temp': res["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
        'icon_text': res["forecast"]["forecastday"][0]["day"]["condition"]["text"],
        'icon': res["forecast"]["forecastday"][0]["day"]["condition"]["icon"],
    }
    return city_info


def get_previous_7days(key, city):
    temp_list = []
    url = "http://api.weatherapi.com/v1/history.json?key={0}&q={1}&dt={2}"
    for i in range(1, 8):
        day =(datetime.today() - timedelta(days=i)).strftime('%Y-%m-%d')
        res = requests.get(url.format(key, city,day)).json()
        temp = res["forecast"]["forecastday"][0]["day"]["avgtemp_c"]
        temp_list.append(temp)
    return temp_list


def update_or_create(city_name, forcast_temp, today_temp, sevenday):
    City_wheather.objects.update_or_create(
        city=city_name,
        forcastday=forcast_temp,
        today=today_temp,
        day_1=sevenday[0],
        day_2=sevenday[1],
        day_3=sevenday[2],
        day_4=sevenday[3],
        day_5=sevenday[4],
        day_6=sevenday[5],
        day_7=sevenday[6],
    )

