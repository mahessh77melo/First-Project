from django.contrib import admin
from django.urls import path
from . import views

app_name='landerapp'
urlpatterns=[
    path('landersignup/',views.sign_up,name='landersignup'),
    path('landerlog/',views.log_in,name='landerlog'),
    path('logout/',views.user_logout,name='landerout'),
]
