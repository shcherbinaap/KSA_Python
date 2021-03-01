# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип
# и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
# в формат Unicode и также проверить тип и содержимое переменных.
# https://www.branah.com/unicode-converter

def str_info(arr):
    for str in arr:
        print(f'Тип строки 1 - {type(str)}. Содержиние переменной - {str}. Длина переменной - {len(str)}')

arr_str = ['разработка', 'сокет', 'декоратор']
arr_str_u = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

str_info(arr_str)
str_info(arr_str_u)

