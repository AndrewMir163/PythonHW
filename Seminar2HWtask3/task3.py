""" Реализуйте алгоритм перемешивания списка. 
НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int """






import random


def Fill_list():
    new_list = []
    for i in range(10):
        new_list.append(i)
    return new_list

my_list = Fill_list()
print(my_list)


def myshuflist(my_list: list):
    size = len(my_list)
    new_i = random.randint(0, size - 1)

    for i in range(size):
        my_list[i], my_list[new_i] = my_list[new_i], my_list[i]


myshuflist(my_list)
print(my_list)


