"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""


class Data:
    date_format = "dd-mm-yyyy"

    def __init__(self, dmy_str):
        self.data = dmy_str

    def print_dmy_str(self):
        print(self.data)

    @classmethod
    def print_data_format(cls):
        print(f"data format is {cls.date_format}")

    @classmethod
    def from_str_to_int(cls, dmy_str):
        dd, mm, yyyy = dmy_str.split(sep='-')
        dd = int(dd)
        mm = int(mm)
        yyyy = int(yyyy)
        return dd, mm, yyyy

    @staticmethod
    def valid_data(dd, mm, yyyy):
        assert 0 < mm < 13, ValueError('Месяц должен быть от 1 до 12!')
        m30 = (4, 6, 9, 11)
        if mm in m30:
            assert 0 < dd < 31, ValueError('День должен быть от 1 до 30!')
        elif mm != 2:
            assert 0 < dd < 32, ValueError('День должен быть от 1 до 31!')
        elif yyyy % 4 == 0:
            assert 0 < dd < 30, ValueError('День должен быть от 1 до 29!')
        else:
            assert 0 < dd < 29, ValueError('День должен быть от 1 до 28!')
        print("Все верно!")

# Проверяем, что создание объекта класса работает
dt1 = Data('5 января 91')
dt1.print_dmy_str()

#из строкового конертируем в числовой
dd, mm, yyyy = Data.from_str_to_int("04-09-1887")
# Проверили работу метода2
try:
    Data.valid_data(dd, mm, yyyy)
except:
    print("Wrong date values")

print("Введите число в формате dd-mm-yyyy")
dt_str = input()
dd, mm, yyyy = Data.from_str_to_int(dt_str)
try:
    Data.valid_data(dd, mm, yyyy)
except:
    print(f"Wrong date values in {dt_str}")
# или
print("Введите число в формате dd-mm-yyyy")
dt_str = input()
dd, mm, yyyy = Data.from_str_to_int(dt_str)
Data.valid_data(dd, mm, yyyy)
