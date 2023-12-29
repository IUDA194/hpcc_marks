from django.contrib import admin
from django.urls import path
from logs.views import log_render, log_view

urlpatterns = [
    path("json/", log_render),
    path("", log_view)
]
