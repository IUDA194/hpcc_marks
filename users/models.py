from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    spreadsheetId = models.CharField(max_length=250)
    sheet_file_key = models.CharField(max_length=250)

class User(models.Model):
    name = models.CharField(max_length=250, primary_key=True)
    password = models.CharField(max_length=250)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

