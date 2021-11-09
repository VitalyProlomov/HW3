import random
from number import *


# real_number.py - содержит функции обработки реального числа.

class Real_number(Number):
    def __init__(self):
        super().__init__()
        # числитель и знаменатель.
        self.numerator = 0
        self.denominator = 1

    # Ввод параметров реального числа из файла.
    def read_number_parameters(self, str_array, position):
        # Должно быт как минимум 2 непрочитанных значения в массиве
        if position >= len(str_array) - 1:
            return 0
        self.numerator = int(str_array[position])
        self.denominator = int(str_array[position + 1])
        position += 2

        if self.denominator == 0:
            print("Incorrect REAL NUMBER. denominator cannot be zero . The REAL NUMBER will be randomly generated.")
            self.generate_parameters()

        return position

    # Генерация параметров реального числа.
    def generate_parameters(self):
        self.numerator = random.randint(-100, 100)
        self.denominator = random.randint(1, 100)
        pass

    # Вывод параметров реального числа в консоль.
    def print(self):
        print(
            "REAL NUMBER: {}/{}, Real representation = {}".format(
                self.numerator, self.denominator, self.get_real_representation()))
        pass

    # Вывод параметров реального числа в файл.
    def write(self, output_stream):
        output_stream.write(
            "REAL NUMBER:  {}/{}, Real representation = {}".format(
                self.numerator, self.denominator, self.get_real_representation()))
        pass

    # Вычисление вещественного представления реального числа.
    def get_real_representation(self):
        return self.numerator / self.denominator
        pass
