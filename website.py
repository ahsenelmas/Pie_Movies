#views.py codes

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Home Page</h1>')

#urls.py codes (this one is migration)

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home)
]

#urls.py codes

"""
URL configuration for website_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls'))
]

#After that I created models

from django.db import models

class Movie(models.Model):
    image = models.CharField(max_length=2083, null=True)  #I added null because it gave error without it.
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    imdb = models.FloatField(null=True)
    duration = models.FloatField(null=True)

#My Database


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#I reorganized install apps because I need to add my apps


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movie.apps.MovieConfig',
]

#Then I opened my database with SQlite
