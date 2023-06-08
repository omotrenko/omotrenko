# 4.Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
# Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Storage:

    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Позиция': self.name, 'Цена за позицию': self.price, 'В наличии': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование')
            unit_p = int(input(f'Введите цену'))
            unit_q = int(input(f'Введите поступление'))
            unique = {'Позиция': unit, 'Цена за позицию': unit_p, 'В наличии': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'


        print(f'Для выхода - stop или стоп, продолжение - нажмите Enter')
        q = input(f'---> ')
        if q == 'stop' or q == 'стоп':
            self.my_store_full.append(self.my_store)
            print(f'На складе -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Storage.reception(self)


class Printer(Storage):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Storage):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Storage):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('ххх', 0000, 0, 00)
unit_2 = Scanner('yyy', 0000, 0, 00)
unit_3 = Copier('zzz', 0000, 0, 00)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_print())
print(unit_3.to_copier())