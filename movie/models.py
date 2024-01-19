from django.db import models

class Movie(models.Model):
    image = models.CharField(max_length=2083, null=True)
    name = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    imdb = models.FloatField(null=True)
    duration = models.FloatField(null=True)