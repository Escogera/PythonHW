# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def factor():
    number = int(input("Введите натуральное число N = "))
    empty_list = []
    k = 2
    while number > 1:
        if number % k == 0:
            empty_list.append(k)
            number /= k
        else:
            k += 1
    print(empty_list)


factor()
