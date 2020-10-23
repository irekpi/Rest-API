from django.urls import path, include
from .api import router

app_name = 'rental'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
