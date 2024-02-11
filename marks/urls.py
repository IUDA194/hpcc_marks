from django.contrib import admin
from django.urls import path, include
from marks.views import lessons, marks_v, users_parse

urlpatterns = [
    path("", marks_v().route),
    path("users_parse/", users_parse().route),
    path("lessons/", lessons().route)
]
