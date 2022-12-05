import httplib2
import os
import pandas

from pandas import *
from apiclient import discovery
from google.oauth2 import service_account
#authorization stuff apparently

class ebayData:
    def __init__(item,initial_price,total_price): #constructor with int
        item.initial_price = initial_price
        item.total_price = total_price
        pass
    def __str__(item):
        return f"{item.initial_price}({item.total_price})" #constructor if string
try:
    scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
    secret_file = os.path.join(os.getcwd(), 'googlesheetsupdater.json')
    spreadsheet_id = '1TZN_sf__aTF2jc0ZmbPy4PeslwUmjI9UeW_19W0hBog'
    range_name = 'Sheet1!A:A' #specify what sheet, ! delimiter and the cells
    credentials = service_account.Credentials.from_service_account_file(secret_file, scopes =scopes)
    service = discovery.build('sheets','v4',credentials=credentials)
    # above line specifies credentials according to waht we pu above

    #below, i was getting erros with a later csv. want to fix later
"""
    extraction = read_csv("OrdersReport.csv", error_bad_lines=False) 
    #filtered_extraction = extraction.dropna(subset=['Unnamed: 11']) #take col 11, which has 
    #print(filtered_extraction['Unnamed: 9'].tolist())
    #values = [
       # extraction['Unnamed: 11'].tolist()
        #extraction.tolist()

   # ] # like a vector/matrix of indexes, and then value to place
    # so right now we have ranges a1-2 to d1-2. for me, make program find out where empty in specified price rows, and then
    #write to it. boom? 
    #11-9 have to read in .csv file and stuff
    #FINISHED
    #ok now we have to write to sheets in one column
    #data = {
      #  'values' : values
   # }

    print(extraction)
    #service.spreadsheets().values().update(spreadsheetID=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()
    print("attempting to write sheets")
    service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()
"""
except OSError as e:
    print(e)
