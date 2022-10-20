# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
# 1 2 2 1 3 4 5 6 6 7 4 -> 3 5 7

first_list = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {first_list}")
second_list = []
last_list = []
for i in range(len(first_list)):
    for j in range(len(first_list)):
        if i == j:
            continue
        else:
            if first_list[i] == first_list[j]:
                second_list.append(i)
for i in range(len(first_list)):
    if i in second_list:
        continue
    else:
        last_list.append(first_list[i])
print(
    f"Cписок неповторяющихся элементов исходной последовательности {last_list}")
