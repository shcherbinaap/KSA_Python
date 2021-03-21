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


def createParser(adr = 'localhost', port = 7777):
    parser = argparse.ArgumentParser()
    # print(parser)
    parser.add_argument('-adr', default = adr)
    parser.add_argument('-port', default = port)
    # print(parser.parse_args())
    return parser.parse_args()

class sock():
    def __init__(self, socket):
        self.s = socket

    def connect(self, adr, port):
        self.s.connect((adr, int(port)))

    def send(self, msg):
        self.s.send(json.dumps(msg, sort_keys = True, indent = 4).encode(ENCODING))

    def recive(self):
        data = self.s.recv(1000000)
        print('Сообщение от сервера: ', (data.decode(ENCODING)), ', длиной ', len(data), 'байт')


def main(msg, adr, port):
    with socket(AF_INET, SOCK_STREAM) as s:
        sock_obj = sock(s)

        sock_obj.connect(adr, int(port))
        sock_obj.send(msg)
        sock_obj.recive()


#         s.send(json.dumps(msg, sort_keys = True, indent = 4).encode(ENCODING))
#         data = s.recv(1000000)
#         print('Сообщение от сервера: ', (data.decode(ENCODING)), ', длиной ', len(data), 'байт')


if __name__ == '__main__':
    parser = createParser()
    # namespace = parser.parse_args(sys.argv[1:])

    msg = {
        "action": "quit",
        "type": "status",
        "user": {
            "account_name": "C0deMaver1ck",
            "status": "Yep, I am here!"
        }
    }

    main(msg, parser.adr, parser.port)


