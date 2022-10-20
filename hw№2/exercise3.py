# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# Пример:

# Для n = 6 -> 14.072



n = int(input('Введите число: '))
sum = 0
if n == 0:
    print("Введите число больше 0")
else:
    for i in range(1, n + 1):
        value = (1 + 1 / i) ** i
        n = round(value, 3)
        sum += n#         
print()
print(f"Сумма чисел последовательности равна: {sum}")

