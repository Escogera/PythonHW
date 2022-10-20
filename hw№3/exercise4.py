# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input("Введите число: "))
list = []
print(f"{num} -> ", end="")
while num > 0:
    temp = num % 2
    num = num//2
    list.append(temp)

list.reverse()

print("".join(map(str, list)))


