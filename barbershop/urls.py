from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('services', views.services, name="services"),
]
