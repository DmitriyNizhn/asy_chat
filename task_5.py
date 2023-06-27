"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
import subprocess
import chardet

ARGS = [['ping', 'yandex.ru'], ['ping', 'youtube.com']]
for ARG in ARGS:
    YA_PING = subprocess.Popen(ARG, stdout=subprocess.PIPE)
    ping_iter = 0
    for line in YA_PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
        ping_iter += 1
        if ping_iter > 5:
            break
