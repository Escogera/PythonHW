# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("Lesson5_2", "w", encoding="UTF-8") as data_file:
    data_file.write("абв вваыаы аавыабв абв ываыва")
with open("Lesson5_2", "r", encoding="UTF-8") as data_file:
    string = data_file.readline().split()
result = list(filter(lambda e: 'абв' not in e, string))
print(result)







