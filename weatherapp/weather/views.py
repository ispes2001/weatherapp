import requests
from django.shortcuts import render

# Create your views here.
def index (request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1d5f3baf25ad4cd0cd850f591c4b7095&units=metric'
    city = 'Nepal'
    r = requests.get(url.format(city))
    data = r.json()
    city_weather = {
        'city' : city,
        'temperature' : data['main'] ['temp'],
        'description' : data['weather'] [0] ['description'],
        'sunrise' : data ['sys'] ['sunrise'],
        'sunset' : data ['sys'] ['sunset'],
        'icon' : data['weather'] [0] ['icon'],
    }
    context = {'city_weather' : city_weather}
    return render (request, 'weather/weather.html', context)
