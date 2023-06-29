#  Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
# сохранение данных в файле YAML-формата. Для этого:
# a. Подготовить данные для записи в виде словаря, в котором первому ключу
# соответствует список, второму — целое число, третьему — вложенный словарь, где
# значение каждого ключа — это целое число с юникод-символом, отсутствующим в
# кодировке ASCII (например, €);
# b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
# При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
# также установить возможность работы с юникодом: allow_unicode = True;
# c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
# с исходными.

import yaml

def data_write_yaml(data):
    with open('data_write.yaml', 'w') as f_n:
        yaml.dump(data, f_n, default_flow_style=True, allow_unicode=True)

    with open('data_write.yaml') as f_k:
        content = yaml.safe_load(f_k)

    return content


data = {
    'item': ['apple', 'orange', 'tomato'],
    'quantity': 23,
    'price': {
        'apple': '5€',
        'orange': '7€',
        'tomato': '5€'
    }
}

print(data_write_yaml(data))

