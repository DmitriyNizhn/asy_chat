# a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
# данными, их открытие и считывание данных. В этой функции из считанных данных
# необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
# каждого параметра поместить в соответствующий список. Должно получиться четыре
# списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
# функции создать главный список для хранения данных отчета — например, main_data
# — и поместить в него названия столбцов отчета в виде списка: «Изготовитель
# системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
# столбцов также оформить в виде списка и поместить в файл main_data (также для
# каждого файла);
# b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
# функции реализовать получение данных через вызов функции get_data(), а также
# сохранение подготовленных данных в соответствующий CSV-файл;
# c. Проверить работу программы через вызов функции write_to_csv().
import csv
import os
import re


def get_data():
    file_list = os.listdir('data')
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    os_name_column = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data = [os_prod_list, os_name_list, os_code_list, os_type_list]
    for file in file_list:
        num = len(main_data)
        with open(f'data/{file}', 'r') as f_n:
            file = f_n.read()
            search_word = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
            while num > 0:
                word = search_word.pop()
                os_prod_reg = re.compile(f'{word}:\s*\S*')
                main_data[num - 1].append(os_prod_reg.findall(file)[0].split()[-1])
                num -= 1
    answ = []
    answ.append(os_name_column)
    i = 0
    while i != (len(main_data[0])):
        line = [main_data[0][i], main_data[1][i], main_data[2][i], main_data[3][i]]
        answ.append(line)
        i+=1

    return answ


def write_to_csv():
    with open('kp_data_write.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in get_data():
            f_n_writer.writerow(row)


write_to_csv()



