"""
Задание 2.

Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя!!! методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

words = ['class', 'function', 'method']

for word in words:
    answ = bytes(word, 'utf-8')
    answ_type = type(answ)
    answ_len = len(answ)
    print(answ, answ_type, answ_len)

