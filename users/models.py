from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=250)
    group = models.CharField(max_length=250)