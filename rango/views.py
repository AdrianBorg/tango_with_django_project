from django.shortcuts import render
from django.http import HttpResponse
from tango_with_django_project.settings import MEDIA_URL
#import os

# Create your views here.


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the tamplate!
    context_dict = {'boldmessage': "Crunchy, creamy cookie, candy, cupcake!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
