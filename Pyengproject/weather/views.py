from django.shortcuts import render
import requests


def get_weather(request):
    key = "d094ea8e2b504d63b38174904210512"
    city = "Москва"
    if request.method == 'POST':
        city = request.POST['city']
    today_city_info = get_whether_today(key, city)
    tomorrow_city_info = get_whether_tomorrow(key, city)
    context = {'today_city_info': today_city_info,
               'tomorrow_city_info': tomorrow_city_info
               }
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
