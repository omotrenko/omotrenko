# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class NumOnlyErr(Exception):
    def __init__(self, text):
        self.text = text


new_list = []
while True:
    try:
        new_item = input('Введите число в список или stop для завершения:')
        if new_item == "stop":
            print(f"обновленный список {new_list}")
            break
        else:
            if not new_item.isdigit():
                raise NumOnlyErr(f"'{new_item}' имеет неверный формат")

            new_item = int(new_item)
            new_list.append(new_item)

    except NumOnlyErr as err:
        print(err)
    else:
        print(new_list)
