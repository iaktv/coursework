import json
from datetime import datetime
from pprint import pprint
from operator import itemgetter

def load_operations():
    """Загружает список транзакций из файла operations.json"""
    with open("operations.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        return data

def get_filter_state(operations):
    """Делает выборку операций по статусу "EXECUTED" """
    list_state = []
    for i in operations:
        if i.get('state') == "EXECUTED":
            list_state.append(i)
    return list_state

def sorts_date(operations):
    """Сортируем список по ключу date и выводим последние 5 выполненных операций"""
    date_key = sorted(operations, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return date_key[:5]

def change_date_format(date):
    transform_date = datetime.fromisoformat(date)
    day_x = datetime.strftime(transform_date, '%d.%m.%Y')
    return day_x

def change_card(number):
    """Маскируем номер карты"""
    number_list = number.split()
    card_number = number_list.pop()
    card_name = number_list
    transform_card_number = f'{" ".join(card_name)} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:17]}'
    return transform_card_number

def change_account(numb):
    """Маскируем номер счета"""
    numb_list = numb.split()
    account_number = numb_list.pop(-1)
    transform_account_number = f"Счет **{account_number[-4:]}"
    return transform_account_number









