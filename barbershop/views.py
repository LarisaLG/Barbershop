from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests import request
from .models import *
from .forms import BookingForm
import datetime


# Create your views here.
def index(request):
    """This view renders the index.html page
    and extends the base.html page
    """
    return render(request, 'index.html')


def services(request):
    """
    This view renders to the user the services page.
    """
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})


def booknow(request):
    """The view for the booking page. If user is logged in it renders the
    booknow.html, otherwise it redirects user to the login page or signup page.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        print("Errors: ", form.errors)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            return redirect('bookings')
    form = BookingForm()
    return render(request, 'booknow.html', {'form': form})


def bookings(request):
    """This view checks if user is logged in and renders the bookings.html
    page which shows user bookings and otherwise it redirects to the signup page
    """
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        context = {
           'bookings': bookings
        }
        return render(request, 'bookings.html', context)
    else:
        return redirect('../accounts/signup')
