# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# # Пример:

# # пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
n = abs(n)
res = 1
if n == 0:
    print("Введите число больше 0")
else:
    for i in range(1, n+1):
        res *= i
        print(res)
