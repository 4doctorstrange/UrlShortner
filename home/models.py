from django.db import models

# Create your models here.

class short_urls(models.Model):
    short_url =  models.CharField(max_length=200)  #it will store the token
    long_url = models.URLField("URL", unique=False, max_length=1000)

