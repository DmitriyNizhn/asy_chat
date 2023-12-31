# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
# информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
# этого:
# a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
# (item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
# должна предусматривать запись данных в виде словаря в файл orders.json. При
# записи данных указать величину отступа в 4 пробельных символа;
# b. Проверить работу программы через вызов функции write_order_to_json() с передачей
# # в нее значений каждого параметра.
#
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open('orders.json') as f_r:
        obj = json.load(f_r)
    for k in obj:
        key = k

    d_json = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    obj[k].append(d_json)
    with open('orders.json', 'w') as f_n:
        json.dump(obj, f_n, sort_keys=True, indent=4)


write_order_to_json(1, 2, 3, 4, 5)
