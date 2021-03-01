# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
# из байтовового в строковый тип на кириллице.

import subprocess
import locale

def site_ping(arg):
    subproc_ping = subprocess.Popen(arg, stdout = subprocess.PIPE)
    for line in subproc_ping.stdout:
        print(line.decode('cp866'))

args = [['ping', 'google.com'], ['ping', 'yandex.ru']]


def_coding = locale.getpreferredencoding()
print(def_coding)

for arg in args:
    site_ping(arg)

