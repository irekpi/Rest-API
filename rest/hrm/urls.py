from django.urls import path
from . import views
from .api import UserList, UserDetail, UserAuthentication

app_name = 'hrm'

urlpatterns = [
    path('user_list/', UserList.as_view(), name='user_list'),
    path('user_list/<employee_id>', UserDetail.as_view(), name='user_detail'),
    path('auth/', UserAuthentication.as_view(), name='User Authentication API'),
]
