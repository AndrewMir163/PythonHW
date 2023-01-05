""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """

x = int(input('Введите значение х: '))
y = int(input('Введите значение y: '))
z = int(input('Введите значение z: '))

def Predicate(x):
    left = not (x or y or z)
    right = not x and not y and not z
    result = left == right
    return result



if Predicate(x) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
