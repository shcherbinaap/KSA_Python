import unittest

from client import createParser


class TestCreateParser(unittest.TestCase):

    def test_createParser_adr_default(self):
        namespace = createParser()
        self.assertEqual(
            namespace.adr,
            'localhost'
        )

    def test_createParser_port_default(self):
        namespace = createParser()
        self.assertEqual(
            namespace.port,
            7777
        )

    def test_createParser_adr(self):
        namespace = createParser(adr = '127.0.0.1')
        self.assertEqual(
            namespace.adr,
            '127.0.0.1'
        )

    def test_createParser_port(self):
        namespace = createParser(port = 1010)
        self.assertEqual(
            namespace.port,
            1010
        )

class TestSock(unittest.TestCase):

    def test_connect(self):
        pass

    def test_send(self):
        pass

    def test_recive(self):
        pass


if __name__ == '__main__':
    unittest.main()