from django.contrib import admin
from . import  views
from django.urls import path

urlpatterns = [
    path('',views.home,name="home-page"),
    path('about',views.about,name="about-page")
]
