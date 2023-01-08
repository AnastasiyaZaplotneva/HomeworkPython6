# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

import random


def create_rand_list(size):
    numbers = []
    for i in range(size):
        numbers.append(random.randint(1, 20))
    return numbers


def filter_list(num, array):
   new_list = [i for i in array if i > num]
   return new_list


lenght = int(input('Укажите количество элементов в списке: '))
first_list = create_rand_list(lenght)
print(first_list)
number = int(input('Укажите базовое значение для сравнения: '))
print(filter_list(number, first_list))