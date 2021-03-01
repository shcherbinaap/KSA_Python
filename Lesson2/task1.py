# 1. Задание на закрепление знаний по модулю CSV.
# Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
# и формирующий новый «отчетный» файл в формате CSV.
# Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью регулярных
# выражений извлечь значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.

# В этой же функции создать главный список для хранения данных отчета — например, main_data — и
# поместить
# в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
# В этой функции реализовать получение данных через вызов функции get_data(),
# а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import csv
from collections import namedtuple
import re

info_struct = namedtuple('info_struct', ['os_prod', 'os_name', 'os_code', 'os_type'])


def get_data_2_(file_list, info_name_list, os_info_list):
    os_info_list[len(os_info_list) - 1].append(info_name_list)
    for file in file_list:
        info_list = ['' for i in range(len(info_name_list))]
        with open(file, 'r') as f_n:
            for row in f_n:
                if row.split(':')[0] in info_name_list:
                    os_info_list[info_name_list.index(row.split(':')[0])].append(row.split(':')[1].strip())
                    info_list[info_name_list.index(row.split(':')[0])] = row.split(':')[1].strip()
        os_info_list[len(os_info_list) - 1].append(info_list)
        # print(f'end {file}')
    return os_info_list


def write_to_csv_(file_list, info_name_list, link_to_file):
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = []

    os_info_list = [os_prod_list, os_name_list, os_code_list, os_type_list, main_data]

    get_data_2_(file_list, info_name_list, os_info_list)
    # print(main_data)
    with open(link_to_file, 'w') as f_csv:
        f_csv_file = csv.writer(f_csv)
        for row in main_data:
            f_csv_file.writerow(row)


def get_data(file_list, info_name_list):
    res = []
    res.append(info_name_list)
    for file_name in file_list:
        with open(file_name, 'r') as input:
            info = []
            for row in input:
                for name in info_name_list:
                    pattern = re.compile(f"^({name})(:\s+)(.*)\n$")
                    result = pattern.findall(row)
                    if result:
                        print(result[0])
                        info.append(result[0][-1])
            if info:
                print(info)
                infotuple = info_struct(*info)
                res.append(infotuple)
    return res


def write_to_csv(file_list, info_name_list, link_to_file):
    main_data = get_data(file_list, info_name_list)
    print(main_data)
    with open(link_to_file, 'w') as f_csv:
        f_csv_file = csv.writer(f_csv)
        for row in main_data:
            f_csv_file.writerow(row)


if __name__ == '__main__':
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    info_name_list = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    link_to_file = 'file_cvs.csv'
    write_to_csv(file_list, info_name_list, link_to_file)
    write_to_csv_(file_list, info_name_list, link_to_file+'and.csv')
