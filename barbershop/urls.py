from django.urls import path, include


from barbershop.views import index

urlpatterns = [
    path('', index),
]
