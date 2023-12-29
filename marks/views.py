from django.shortcuts import render
from django.http import JsonResponse
from dotrest.DOTREST import Simple_View, Serialyzers
from marks.marks import table

class lessons(Simple_View):
    def get(self, request):
        result = table().get_sheets()

        return JsonResponse({"status" : True, 
                             "data" : result})
    
class marks_v(Simple_View):
    def get(self, request):

        user_name = request.GET.get("name")
        lesson = request.GET.get("lesson")

        result = table().get_data(lesson)

        return JsonResponse({"status" : True, 
                             "data" : result[user_name]})