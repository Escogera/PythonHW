#  2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


list_length = int(input("Введите размерность списка "))


def new_list_creation(lst_length):
    lst = []
    for i in range(lst_length):
        new_number = random.randint(-10, 11)
        lst.append(new_number)
    return lst


list = new_list_creation(list_length)
print(f"Результат случайного заполнения списка: {list}")


def multip_two_opposite_numbers(list, list_length):
    lst = []
    if list_length % 2 == 0:
        for i in range(list_length//2):
            result = list[i] * list[list_length - 1 - i]
            lst.append(result)
        print(f'Результат умножения равен: {lst}')
    else:
        for i in range((list_length + 1)//2):
            result = list[i] * list[list_length - 1 - i]
            lst.append(result)
        print(f'Результат умножения равен: {lst}')


multip_two_opposite_numbers(list, list_length)
