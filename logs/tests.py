import os

logs = []
with open("/Users/aroslavgladkij/Documents/GitHub/matex_back/matex/logs/test.log", 'r') as log_file:
    logs = log_file.readlines()

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
    

print(Logs().convert(logs))