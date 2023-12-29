from django.shortcuts import render
from django.http import response
import os
import json
from django.http import JsonResponse
import logging

class Logs:
    def __init__(self) -> None:
        self.result = []
        self.log = {}
        self.log["message"] = ""
        self.log["detail"] = []

    def convert(self, logs) -> dict:
        for i in logs:
            if i.startswith("ERROR") or i.startswith("INFO") or i.startswith("WARNING") or i.startswith("DEBUG"): 
                print(self.log["message"], "|", len(self.log["detail"]))
                self.result.append({"message" : self.log["message"],
                                    "last_deteil" : self.log["detail"]})
                self.log["message"] = i
                self.log["detail"] = []
            else:
                self.log["detail"].append(i)
        print(self.log["message"], "|", len(self.log["detail"]))
        self.result.append({"message" : self.log["message"],
                                "last_deteil" : self.log["detail"]})
        return self.result

def log_render(request):
    logs = []
    with open(os.getenv("LOGS_PATH"), 'r') as log_file:
        logs = log_file.readlines()

    logs_formated = Logs().convert(logs[::-1])
    return JsonResponse(logs_formated)


def log_view(request):

    logs = []
    with open(os.getenv("LOGS_PATH"), 'r') as log_file:
        logs = log_file.readlines()

    logs_formated = Logs().convert(logs)

    print(logs_formated)

    return render(request, 'logs.html', {'logs': logs_formated[::-1]})
