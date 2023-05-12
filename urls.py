from django.urls import path
from weather_app.views import weather_forecast

urlpatterns = [
    path('', weather_forecast, name='weather_forecast'),
]
