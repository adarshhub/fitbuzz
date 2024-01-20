from django.urls import path, include
from . import apis as app_apis

name = "app"
urlpatterns = [
    path('fitbuzz', app_apis.FizzBuzzRequest.as_view(), name="fitbuzz-request"),
    path('stats', app_apis.Stats.as_view(), name="stats" )
]
