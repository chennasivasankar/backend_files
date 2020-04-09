from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request,actor_id1):
    director_obj=Director()
    return Movie.objects.all(director=director_obj)
    