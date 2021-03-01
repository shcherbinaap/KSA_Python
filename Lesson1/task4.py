# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

arr_str = ['attribute', 'класс', 'функция', 'type']

for str in arr_str:
    str_bite = str.encode('utf-16')
    str_from_bite = str_bite.decode('utf-16')
    print(f'Строка "{str}" преобразована в набор байтов и имеет вид - {str_bite}. Обратное преобразование дает строку - {str_from_bite}')

