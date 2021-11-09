from math import sqrt
from number import *


# polar_coordinates.py - содержит функции обработки вещественных координат.

class Polar_coordinates(Number):

    def __init__(self):
        super().__init__()
        # Координаты вершин.
        self.length = 0
        self.radians = 0


    # Ввод параметров вещественных координат из файла.
    def read_number_parameters(self, str_array, position):
        # Должно быть как минимум 2 непрочитанных значения в массиве
        if position >= len(str_array) - 1:
            return 0
        self.length = int(str_array[position])
        self.radians = int(str_array[position + 1])
        position += 2

        return position

    # Генерация параметров вещественных координат
    def generate_parameters(self):
        self.length = random.randint(-20, 20)
        self.radians = random.randint(-20, 20)

        pass

    # Вывод параметров вещественных координат в консоль.
    def print(self):
        print(
        "POLAR COORDINATES. Length: {}, radians: {}. Real representation = {}".format(
            self.length, self.radians, self.get_real_representation()))
        pass

    # Вывод параметров вещественных координат в файл.
    def write(self, output_stream):
        output_stream.write(
            "POLAR COORDINATES. Length: {}, radians: {}. Real representation = {}".format(
                self.length, self.radians, self.get_real_representation()))
        pass

    # Вычисление вещественного представления вещественных координат.
    def get_real_representation(self):
        return self.length
        pass
