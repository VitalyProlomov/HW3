import random

from real_number import Real_number
from complex_number import Complex_number
from polar_coordinates import Polar_coordinates


# build_container.py - содержит функцию ввода данных.

# Ввод содержимого контейнера.
def build_container(container, str_array):
    array_length = len(str_array)
    # Если параметров меньше пяти, то чисел нет.
    if array_length < 3:
        return 0
    # Текущая позиция при чтении параметров фигур.
    position = 0
    number_index = 0
    while position < array_length:
        # Получение ключа - номера фиуры.
        key = int(str_array[position])
        # Значение ключа для комплекснрого числа
        if key == 1:
            number = Real_number()
        # Значение ключа для реальног числа.
        elif key == 2:
            number = Complex_number()
        # Значение ключа для полярных коорд-т.
        elif key == 3:
            number = Polar_coordinates()
        else:
            # Некорректный ключ признака. Возвращаем количество уже прочитанных чисел
            return number_index

        position += 1
        if position == array_length:
            return number_index

        # Чтение параметров числа с возвратом позиции после него.
        position = number.read_number_parameters(str_array, position)
        if position == 0:
            return number_index
        number_index += 1
        container.store.append(number)
    return number_index
