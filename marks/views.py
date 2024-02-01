from django.shortcuts import render
from django.http import JsonResponse
from dotrest.DOTREST import Simple_View, Serialyzers
from marks.marks import table

arr = ["П", "вфівф"]

class lessons(Simple_View):
    def get(self, request):
        result = table().get_sheets()

        for i in arr:
            try: result.remove(i)
            except: pass

        return JsonResponse({"status" : True, 
                             "data" : result})
    
class marks_v(Simple_View):
    def get(self, request):

        user_name = request.GET.get("name")
        lesson = request.GET.get("lesson")

        result = table().get_data(lesson)

        return JsonResponse({"status" : True, 
                             "data" : result[user_name][::-1]})