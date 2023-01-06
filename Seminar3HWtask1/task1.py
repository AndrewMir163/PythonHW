
""" Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
Пример:
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12 """




my_list = []

def Fill_list():
    new_list = []
    for i in range(15):
        new_list.append(i)
    return new_list

my_list = Fill_list()
print(my_list)


def sum_index(my_list):
    s = 0
    for i in range(len(my_list)):
        if i % 2 != 0:
            s += my_list[i]
    print(f"Сумма равна: {s}")


sum_index(my_list)
