# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


def code(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
            if count == 9:
                res = res + str(count) + txt[i]
                count = 0
        else:
            res = res + str(count) + txt[i]
            count = 1      
    if count > 0 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decode(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = input("Введите текст для кодировки: ")
print(f"Текст после кодировки: {code(s)}")
print(f"Текст после дешифровки: {decode(code(s))}")