# Задание 5 Реализуйте алгоритм перемешивания списка.


from random import shuffle


num = int(input('Введите размерность списка, n = '))
arr = []
for i in range(num):
    arr.append(i)
print(arr)
shuffle(arr)
print(arr)
