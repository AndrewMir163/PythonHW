""" Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15] """


my_list = []

def Fill_list():
    new_list = []
    for i in range(4):
        new_list.append(i)
    return new_list

my_list = Fill_list()
print(my_list)

def multiplication_list(my_list):
    main_formula = len(my_list)//2 + 1 if len(my_list) % 2 != 0 else len(my_list)//2
    new_lst = [my_list[i]*my_list[len(my_list)-i-1] for i in range(main_formula)]
    print(new_lst)


multiplication_list(my_list)
