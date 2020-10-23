from django.shortcuts import render
import requests


def geoapi(request):
    response = requests.get(
        'http://api.ipstack.com/134.201.250.155?access_key=de3db3b741c72521c8e3e30a65ac8bf6&output=json'
    )
    geodata = response.json()
    return render(request, 'geoloc.html', context={
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'api_key': 'de3db3b741c72521c8e3e30a65ac8bf6'
    })
