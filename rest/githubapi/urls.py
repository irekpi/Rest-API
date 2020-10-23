from django.urls import path
from . import views

app_name = 'githubapi'

urlpatterns = [
    path('', views.github, name='github'),
]
