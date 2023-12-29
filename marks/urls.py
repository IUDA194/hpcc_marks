from django.contrib import admin
from django.urls import path, include
from marks.views import lessons, marks_v

urlpatterns = [
    path("", marks_v().route),
    path("lessons/", lessons().route)
]
