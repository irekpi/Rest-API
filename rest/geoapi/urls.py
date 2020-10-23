from django.urls import path
from . import views

app_name = 'geoapi'

urlpatterns = [
    path('', views.geoapi, name='geoapi'),
]
