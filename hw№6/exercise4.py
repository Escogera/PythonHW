# 2. Напишите программу, удаляющую из текста все слова, содержащие "абв". <- filter

# -------------Старый код-------------------

# str_ = ("abc dddsrb dddbsrl aaabcdde")
# print (str_)
# list_ = list(map(str, str_.split()))

# # def true_or_not(str_):
# #     return 'abc' in str_   

# # result = filter(true_or_not, list_)
# # for i in result:
# #     print(i)

# --------------Новый код-------------------

str_ = ("abc dddsrb dddbsrl aaabcdde")
print (str_)
list_ = list(map(str, str_.split()))

result = list(filter(lambda e: 'abc' not in e, list_))
print(result)