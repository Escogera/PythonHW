# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#[Негафибоначчи]


num = int(input("Введите число: "))


def negafib(num):
    a = 1
    b = 1
    list_num = [0]
    for i in range(num):
        list_num.append(a)
        list_num.insert(0, a * (-1) ** i)
        sum = a + b
        a = b
        b = sum

    print(list_num)


negafib(num)
