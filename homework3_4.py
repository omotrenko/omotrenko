# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    return x ** y


print(
    f' Результат первого способа: {my_func(int(input("Введите x: ")), int(input("Введите y: ")))}')


def my_func_2(x, y):
    counter = 1
    result = 1 / x
    while counter < abs(y):
        result = result * (1 / x)
        counter += 1
    return result


print(
    f'Результат второго способа: {round(my_func_2(int(input("Введите x: ")), int(input("Введите y: "))), 2)}')
