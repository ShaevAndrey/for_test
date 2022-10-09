import os
import requests
import gspread
import xmltodict
from dotenv import load_dotenv
from .models import OrderTable


mem_data = {}
load_dotenv()


def memo(func):
    def wrapper(data):
        if data not in mem_data:
            mem_data[data] = func(data)        
        return mem_data[data]
    return wrapper

def connect_to_sheet():
    sa = gspread.service_account('cred.json')
    sheet = sa.open('тестовое')
    return sheet
    

@memo
def get_change_kurs(data:str) ->float :
    response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp')
    data = response.content
    data = xmltodict.parse(data)
    for valute in data['ValCurs']['Valute']:
        if valute['@ID'] == 'R01235':
            value = valute['Value'].replace(',', '.')
            return float(value)
    return None

def get_table_from_server() ->list:
    w_sheet =connect_to_sheet().worksheet('Лист1')
    data = w_sheet.get_all_records()
    return data

def get_table_from_base() ->list:
    return OrderTable.objects.all()

def check_update() -> bool:
    last_time = os.getenv('UPDATE_TIME', None)
    sheet =connect_to_sheet()
    curren_time = sheet.lastUpdateTime
    if last_time != curren_time:
        os.environ['UPDATE_TIME'] = curren_time
        return True
    return False

def compare_table(table):
    pass

def update_table(new_table, kurs):
    OrderTable.objects.all().delete()
    for row in new_table:
        OrderTable(id=row['№'], order_id=row['заказ №'], cost_usd=row['стоимость,$'], cost_rub=int(row['стоимость,$'])*kurs, delivery_date=row['срок поставки']).save()