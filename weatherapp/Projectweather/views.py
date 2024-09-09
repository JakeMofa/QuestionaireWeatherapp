from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import requests
from .models import City

def get_weather(request):
    api_key = 'your_api_key_here'
    weather_data = None.
    error_message = None

    if request.method == 'POST':
        city = request.POST['city']
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            print(weather_data)
        else:
            error_message = "City not found or API error."

    return render(request, 'weather.html', {'weather': weather_data, 'error': error_message})


## def getweather(request):
api_