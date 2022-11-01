from django.shortcuts import render
from django.http import HttpResponse
from requests import request
from .models import *


# Create your views here.
def index(request):
    """This view renders the index.html page
    and extends the base.html page
    """
    return render(request, 'barbershop/index.html')


def services(request):
    """
    This view renders to the user the services page.
    """
    return render(request, 'barbershop/services.html')


def booknow(request):
    """The view for the booking page. If user is logged in it renders the
    booknow.html, otherwise it redirects user to the login page or signup page.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('my_bookings')
        else:
            form = BookingForm()
            context = {'form': form}
    return render(request, 'barbershop/booknow.html')


def my_bookings(request):
    return render(request, 'barbershop/bookings.html')
