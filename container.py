# container.py - содержит тип данных, представляющий простейший контейнер.

class Container:
    # Максимальная длина массива.
    MAX_LENGTH = 10000

    def __init__(self):
        # Массив чисел.
        self.store = []
        pass

    # Выводит фигуры в консоль.
    def print(self):
        for i in range(len(self.store)):
            print("{}. ".format(i + 1), end='')
            self.store[i].print()
        pass

    # Вывод содержимого контейнера в указанный поток.
    def write(self, output_stream):
        for i in range(len(self.store)):
            output_stream.write("{}. ".format(i + 1))
            self.store[i].write(output_stream)
            output_stream.write("\n")
        pass

    # Перемещение всех чисел с вещественным представлением больше среднего в конец конейнера
    def sort_larger_elements(self):
        all_real_representations = []
        average_real_representation = 0.0
        for number in self.store:
            real_representation = number.get_real_representation()
            all_real_representations.append(real_representation)
            average_real_representation += real_representation

        average_real_representation /= len(self.store)
        new_store = []
        # Adding elements with real representation less than average.
        for i in range(len(all_real_representations)):
            if all_real_representations[i] <= average_real_representation:
                new_store.append(self.store[i])

        for i in range(len(all_real_representations)):
            if all_real_representations[i] > average_real_representation:
                new_store.append(self.store[i])
        self.store = new_store
        return average_real_representation
