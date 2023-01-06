""" Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
Пример:
Для n=4 -> [2, 2.25, 2.37, 2.44] """




""" Почему не работает этот код??? """


""" n = int(input("Введите число: "))

print('[', sep = '')
 
for i in range (1, n + 1):
    result = round((1 + 1 / n)**n, 3)
    sum = float(sum([res for res in range(i + 1)]))
    if i < (n + 1) -1: 
        print(f'{sum}', end = ', ')
    else: print(f'{sum}', end = '')
print(']', end = '') """

""" Рабочий код, выполнил с помощью гуглежа(
 """

n = int(input("Введите число: "))

list = [round((1+1/i)**i, 3) for i in range(1, n+1)]

print(f'Последовательность: {list}\nСумма: {round(sum(list), 3)}')
