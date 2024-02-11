from django.shortcuts import render
from django.http import JsonResponse
from dotrest.DOTREST import Simple_View, Serialyzers
from marks.password import generate_password
from marks.marks import table
from users.models import User, Group
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
    
class users_parse(Simple_View):
    def get(self, request):

        g = Group.objects.all()

        for data in g:
            shhets = table(key_file=data.sheet_file_key, spreadsheetId=data.spreadsheetId).get_sheets()
            users = table(key_file=data.sheet_file_key, spreadsheetId=data.spreadsheetId).get_data(shhets[0])
            for i in users.keys():
                if not User.objects.filter(name=i).exists():
                    User.objects.get_or_create(
                        name=i,
                        password=generate_password(24),
                        group=Group.objects.filter(name=data.name).get()
                    )
                else: print("pass")
        return JsonResponse({"status" : True})