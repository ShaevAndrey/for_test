import os
from datetime import date
from django.http import JsonResponse

from .serialaizer import OrderTabSerializer
from .servises import *


def get_table(requests):
    kurs = get_change_kurs(date.today())
    if check_update():
        table = get_table_from_server()
        update_table(table, kurs)
    serializer = OrderTabSerializer(get_table_from_base(), many=True)
    return JsonResponse(serializer.data, safe=False)



