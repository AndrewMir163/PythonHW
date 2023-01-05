num = int(input("Введите число: "))

def checkNumber(num):
    if 6 <= num <= 7:
        print("Выходной")
    elif 0 < num < 6:
        print("опять работа(")
    else:
        print("число за пределом 7 дней")


checkNumber(num)