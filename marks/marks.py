import httplib2 
from googleapiclient.discovery import build
import googleapiclient as apiclient
from oauth2client.service_account import ServiceAccountCredentials	
import os

class table:
    path = os.getenv("KEY_FILE_PATH")
    spreadsheetId = "1rbQe4whW1oz5EOnjjfhPMzmIme-4N9lx8o1hSzOtNgM"
    
    service = None
    httpAuth = None
    credentials = None
    sheet_name = None

    def __init__(self) -> None:
        CREDENTIALS_FILE = self.path  # Имя файла с закрытым ключом, вы должны подставить свое
        self.spreadsheetId = "1rbQe4whW1oz5EOnjjfhPMzmIme-4N9lx8o1hSzOtNgM"
        # Читаем ключи из файла
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

        self.httpAuth = self.credentials.authorize(httplib2.Http()) # Авторизуемся в системе
        self.service = build('sheets', 'v4', http=self.httpAuth) # Выбираем работу с таблицами и 4 версию API 

    def transform_data(self, input_data):
        output_data = {}
        
        for row in input_data[1:]:
            student_name = row[0].strip()
            marks = []
            
            for i in range(1, len(row)):
                date = input_data[0][i].strip()
                mark = str(row[i]).strip()
                
                marks.append({'date': date, 'mark': mark})
            
            output_data[student_name] = marks
        
        return output_data


    def get_data(self, sheet : str = None):
        self.sheet_name = sheet

        ranges = f"{self.sheet_name}!A1:AX50"  # Обновляем ranges на основе выбранного листа

        results = self.service.spreadsheets().values().batchGet(spreadsheetId=self.spreadsheetId, ranges=ranges, valueRenderOption='FORMATTED_VALUE', dateTimeRenderOption='FORMATTED_STRING').execute()

        sheet_values = results['valueRanges'][0]['values']

    
        return self.transform_data(sheet_values)


    def get_sheets(self):
        spreadsheet = self.service.spreadsheets().get(spreadsheetId = self.spreadsheetId).execute()
        sheetList = spreadsheet.get('sheets')

        result = []

        for sheet in sheetList:
            result.append(sheet['properties']['title'])

            # print(sheet['properties']['sheetId'], sheet['properties']['title'])

        return result