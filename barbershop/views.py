from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """This view renders the index.html page
    and extends the base.html page
    """
    return render(request, 'barbershop/index.html')


def services(request):
    """
    This view rendes to the user  the services page.
    """
    return render(request, 'services.html')
