# Генерация случайного числа.
import random

from real_number import Real_number
from complex_number import Complex_number
from polar_coordinates import Polar_coordinates


# random_generate_number.py - содержит функцию генерации случайного числа.

# Генерирует случайное число.
def random_generate_number():
    key = random.randint(1, 3)
    # Значение ключа для комплекснрого числа
    if key == 1:
        number = Complex_number()
    # Значение ключа для реальног числа.
    elif key == 2:
        number = Real_number()
    # Значение ключа для полярных коорд-т.
    else:
        number = Polar_coordinates()

    number.generate_parameters()
    return number
