from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

class Simple_View:
    @csrf_exempt
    def route(self,request):
        match request.method:
            case "GET":                 
                #try: 
                return self.get(request)
                #except AttributeError: return self.else_m(request)
            case "POST": 
                try: return self.post(request)
                except AttributeError: return self.else_m(request)
            case "PUT": 
                try: return self.put(request)
                except AttributeError: return self.else_m(request)
            case "PATCH": 
                try: return self.patch(request)
                except AttributeError: return self.else_m(request)
            case "DELETE": 
                try: return self.delete(request)
                except AttributeError: return self.else_m(request)
            case "HEAD": 
                try: return self.head(request)
                except AttributeError: return self.else_m(request)
            case "OPTION": 
                try: return self.option(request)
                except AttributeError: return self.else_m(request)
            case _: return self.else_m(request)
    def else_m(self, request): return JsonResponse({"error" : f"{request.method} is not allowed"}, status = 405)
    



class Serialyzers:

    def __init__(self, model) -> None:
        self.model = model

    def serialyze(self, only_read_fields : list = []) -> dict:
        result = {
            "status" : True
        }
        
        try:
            objects_list = []
            for i in self.model.values():
                if not i in only_read_fields:
                    objects_list.append(i)

            result["data"] = objects_list
        except AttributeError:
            model_dict = vars(self.model)
            model_dict.pop("_state")
            
            for i in only_read_fields:
                model_dict.pop(i)

            result["data"] = [model_dict]
        

        return result