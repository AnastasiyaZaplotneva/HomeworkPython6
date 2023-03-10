# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

import random


def create_list(limit):
    numbers = [i for i in range(20, limit+1) if i%20 == 0 or i%21 == 0]
    return numbers


lim = int(input('Укажите верхнюю границу чисел: '))
first_list = create_list(lim)
print(first_list)
