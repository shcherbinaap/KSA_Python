# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

def sum_user_num(user_num):
    n = user_num
    nn = user_num * 2
    nnn = user_num * 3
    result = int(n) + int(nn) + int(nnn)
    print(result)
    return result


def test_sum_user_num():
    assert sum_user_num('3') == 369, 'Не верная сумма'


# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
def max_num(user_num):
    max_num = 0
    n = 0
    while True:
        num = int((user_num / (10 ** n)) % 10)
        if num == 0:
            break
        elif num > max_num:
            max_num = num
        n += 1
    print(max_num)
    return max_num

def test_max_num():
    assert max_num(132564) == 6, 'Не верное число'

if __name__ == '__main__':
    # user_num = input("Введите число: ")
    # sum_user_num(user_num)

    test_sum_user_num()
    test_max_num()


