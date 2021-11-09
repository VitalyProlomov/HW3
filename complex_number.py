from math import sqrt

from number import *


# complex_number.py - содержит описание комплексного числа.

class Complex_number(Number):
    def __init__(self):
        # реальная и вещественная часть числа.
        self.real_part = 0
        self.imaginary_part = 0

    # Ввод параметров комплексного числа из файла.
    def read_number_parameters(self, str_array, position):
        # Должно быт как минимум 2 непрочитанных значения в массиве
        if position >= len(str_array) - 1:
            return 0
        self.real_part = int(str_array[position])
        self.imaginary_part = int(str_array[position + 1])
        position += 2

        return position

    # Генерация параметров треугольника.
    def generate_parameters(self):
        import random
        self.real_part = random.randint(-20, 20)
        self.imaginary_part = random.randint(-20, 20)
        pass

    # Вывод параметров комплексного числа в консоль.
    def print(self):
        print("COMPLEX NUMBER. Real part: {}, Imaginary part: {}, Perimeter = {}".format(
            self.real_part, self.imaginary_part, self.get_real_representation()))
        pass

    # Вывод параметров комплексного числа в файл.
    def write(self, output_stream):
        output_stream.write("COMPLEX NUMBER. Real part: {}, Imaginary part: {}, Perimeter = {}".format(
            self.real_part, self.imaginary_part, self.get_real_representation()))
        pass

    # Вычисление периметра комплексного числа.
    def get_real_representation(self):
        return sqrt(self.real_part*self.real_part + self.imaginary_part*self.imaginary_part)
        pass
