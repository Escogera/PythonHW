# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""


from random import randint


sweet = int(input("Введите число большее 28\n"))

flag = randint(0,2)
if flag:
    print(f"Первым начинает Игрок")
else:
    print(f"Первым начинает Компьютер")

if flag:
    while sweet >= 28:
        user_one = int(input("Игрок. Ввведите число меньше или равно 28: "))
        if user_one > 28:
            user_one = int(input("Не то число, введите < 28: "))
        sweet -= user_one
        print("Осталось", sweet)
        if sweet == 0:
            print("Вы победили")
            break
        else: 
            user_two = sweet % 29
            print("Компьютер ввел число: ", user_two)
            sweet -= user_two
            print("Осталось", sweet)
            if sweet <= 28:
                print("Победил компьютер")
                break
else:
    while sweet >= 28:
        user_two = sweet % 29
        print("Компьютер ввел число: ", user_two)
        sweet -= user_two
        print("Осталось", sweet)
        if sweet <= 28:
            print("Победил компьютер")
            break
        else:
            user_one = int(input("Игрок. Ввведите число меньше или равно 28: "))
            if user_one > 28:
                user_one = int(input("Не то число, введите < 28: "))
                sweet -= user_one
                print("Осталось", sweet)
                if sweet == 0:
                    print("Вы победили")
                    break

