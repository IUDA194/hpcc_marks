from django.shortcuts import render
from django.http import JsonResponse
from dotrest.DOTREST import Simple_View, Serialyzers
from users.models import User
import json


class user_v(Simple_View):
    def get(self, request):
        name = request.GET.get("name")
        password = request.GET.get("password")

        obj = User.objects.filter(name = name)

        if obj.exists():
            obj = obj.get()

            if password == obj.password:
                return JsonResponse(Serialyzers(obj).serialyze())
            else: return JsonResponse({"status" : False}, status=401)
        else: return JsonResponse({"status" : False}, status=404)

    def post(self, request):

        data = json.loads(request.body.decode('utf-8')) 

        name = data.get("name")
        password = data.get("password")
        group = data.get("group")

        obj = User.objects.filter(name = name)

        if not obj.exists():
            obj = User.objects.create(
                name = name,
                password = password,
                group = group
            ).save()
            return JsonResponse({"status" : True})
        else: return JsonResponse({"status" : False}, status=409)

def login_page(request):
    return render(request, "login.html")

def mark_page(request):
    return render(request, "marks.html")