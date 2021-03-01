# Функции сервера:
#   принимает сообщение клиента;
#   формирует ответ клиенту;
#   отправляет ответ клиенту;
#   имеет параметры командной строки:
#       -p <port> — TCP-порт для работы (по умолчанию использует 7777);
#       -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).


from socket import *
from contextlib import closing
import sys
import argparse

ENCODING = 'utf-8'


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', default = 'localhost')
    parser.add_argument('-p', default = 7777)
    return parser


def sock(adr, port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((adr, port))
        s.listen(5)

        while True:
            client, adr = s.accept()
            with closing(client) as cl:
                data = cl.recv(1000000)
                print('Сообщение: ', data.decode(ENCODING), ', было отправлено клиентом: ', adr)
                msg = 'Привет, клиент!!!'
                cl.send((msg.encode(ENCODING)))


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    sock(namespace.a, int(namespace.p))
