from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def home(request):
    movie = Movie.objects.all()
    return render(request, 'home.html', {'movie': movie})

