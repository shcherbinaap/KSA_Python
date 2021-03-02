# Функции клиента:
#   сформировать presence-сообщение;
#   отправить сообщение серверу;
#   получить ответ сервера;
#   разобрать сообщение сервера;
#   параметры командной строки скрипта client.py <addr> [<port>]:
#       adr — ip-адрес сервера;
#       port — tcp-порт на сервере,
#       по умолчанию 7777.
# import unix

ENCODING = 'utf-8'

from socket import *
import sys
import argparse
import json


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-adr', default = 'localhost')
    parser.add_argument('-port', default = 7777)
    return parser


def sock(msg, adr, port):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect((adr, int(port)))

        s.send(json.dumps(msg, sort_keys = True, indent = 4).encode(ENCODING))
        data = s.recv(1000000)
        print('Сообщение от сервера: ', (data.decode(ENCODING)), ', длиной ', len(data), 'байт')


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    msg = {
        "action": "presence",
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
        }
    }
    sock(msg, namespace.adr, namespace.port)
