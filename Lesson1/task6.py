# 6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл
# в формате Unicode и вывести его содержимое.

file_open_1 = open("test_file.txt", "w")
file_open_1.write("сетевое программирование \nсокет \nдекоратор")
file_open_1.close()
print(file_open_1)


try:
    with open('test_file.txt', encoding='utf-8') as file_open_2:
        for str in file_open_2:
            print(str, end = '')
except UnicodeDecodeError:
    print(f'Файл записан в кодировке "{file_open_1.encoding}", измените кодировку при открытии файла')
