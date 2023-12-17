# example/views.py
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .models import Ice_cream

def index(request):
    """The home page for the website."""
    ice_creams = Ice_cream.objects.all()
    context = {'ice_creams': ice_creams}
    return render(request, 'example/index.html' ,context)

def details (request, ice_id):
    """A view that shows more information about a specific ice cream flavor."""
    ice_id = Ice_cream.objects.get(pk=ice_id)
    context = {'ice_id' : ice_id}
    return render(request,'example/details.html', context)