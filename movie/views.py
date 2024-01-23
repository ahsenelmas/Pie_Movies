from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})