from django.contrib import admin
from django.urls import path
from . import views

app_name="myApp"

urlpatterns = [
    path("index/", views.index, name='index'),
    path("details/", views.details, name='details'),
]