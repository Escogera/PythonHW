# 7.	Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('x y z  ¬(X ⋁ Y ⋁ Z)   ¬X ⋀ ¬Y ⋀ ¬Z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f1 = not(x or y or z)
            f2 = not x and not y and not z
            print(f"\n{x} {y} {z}      {bool(f1)}           {bool(f2)}")
if not(x or y or z) == (not x and not y and not z):
    print("\nУтверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат")
else:
    print("\nУтверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  не для всех значений предикат")

