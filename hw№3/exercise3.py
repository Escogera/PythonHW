# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

list_length = int(input("Введите размерность списка "))


def Filled_list(list_length):
    lst = []
    for i in range(list_length):
        new_number = round(random.random() * 10, 2)
        lst.append(new_number)
    return (lst)


list = Filled_list(list_length)
print(f"Исходный список: {list}")


def new_list(list):
    lst2 = []
    for i in range(len(list)):
        res = round((list[i] % 1), 2)
        lst2.append(res)
    return lst2


list2 = new_list(list)
print(f"Список из значений дробной части элементов: {list2}")
max = list2[0]
min = list2[0]
for i in range(len(list2)):
    if list2[i] >= max and list2[i] != 0:
        max = list2[i]
    elif list2[i] <= min and list2[i] != 0:
        min = list2[i]
print(f"Максимальное значение равно: {max}")
print(f"Минимальное значение равно: {min}")
result = max - min
print(f"Разница между максимальным и минимальным значением дробной части элементов равна {result}")
