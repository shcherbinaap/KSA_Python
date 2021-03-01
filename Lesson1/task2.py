# 2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
# последовательность кодов (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

def str_info(arr):
    for str in arr:
        print(f'Тип строки 1 - {type(str)}. Содержиние переменной - {str}. Длина переменной - {len(str)}')

arr_str = [b'class', b'function', b'method']


str_info(arr_str)