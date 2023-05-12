import requests
from django.shortcuts import render

def weather_forecast(request):
    api_key = "YOUR_API_KEY"
    city = "New York"  # Change it to the desired city

    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=5"
    response = requests.get(url)
    data = response.json()

    current_weather = data["current"]
    forecast = data["forecast"]["forecastday"]

    context = {
        "current_weather": current_weather,
        "forecast": forecast,
    }

    return render(request, "weather_app/weather.html", context)
