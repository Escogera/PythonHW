#  1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

list_length = int(input("Введите размерность списка "))


def list_creation(lst_length):
    lst = []
    for i in range(lst_length):
        new_number = random.randint(0, 11)
        lst.append(new_number)
    return lst


list = list_creation(list_length)
sum = 0
for i in range(list_length):
    if i % 2 != 0:
        sum += list[i]

print(f"{list} -> сумма элементов списка стоящих на нечётной позиции равно: {sum}")
