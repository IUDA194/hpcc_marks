from django.contrib import admin
from django.urls import path, include
from users.views import user_v, login_page, mark_page

urlpatterns = [
    path("", user_v().route),
    path("page/", login_page),
    path("mark/", mark_page)
]
