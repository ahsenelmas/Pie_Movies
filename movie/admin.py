from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name','type','duration','imdb')
    

admin.site.register(Movie, MovieAdmin)
