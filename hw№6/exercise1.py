# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11

# ____Старый код______

# num = input('Введите вещественное число: ')
# for i in num:
#     if i.isdigit():
#         sum += int(i)
# print(sum)

# ____Новый код______

num = input('Введите вещественное число: ')
lst = [int(x) for x in num if x.isdigit()]

print('сумма элементов числа равна: ', sum(lst))