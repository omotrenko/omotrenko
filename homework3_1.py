# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def calculation(var1, var2):
    res = var1 / var2
    return res


try:
    var1 = float(input('Ведите первую переменную:'))
    var2 = float(input('Ведите вторую переменную:'))
    res = calculation(var1, var2)
except ZeroDivisionError:
    print('Не делим на ноль')
else:
    print(res)
