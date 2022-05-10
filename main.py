#############################
#
# Задача 1
#
# создать список функцию потом в эту функцию параметром список потом проверяется

# list = [11, 4, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
# def somefunc(list):
#     b = 0
#     for i in list:
#         if i <30 and i%3== 0:
#             print(i)
#         else:
#             b += i
#     return b


# print('сумма не удостоверяющих условию', somefunc(list))

##########################

# Задача 2

# sum_range(start, end)
# def somefunc(start, end):
#     if start > end:
#         start, end = end, start
#     return sum(range(start,end +1))


# print(somefunc(10,7))

############
# Задача 3

# def more_than_five(func):
#     int(func.sort(key = lambda x: x % 5))
#     return

##################

# x = input()
# y = ''.join(map(str, x))
# z = int(y)


# def more_than_five(z):
#     if z <= 5 or -z >= 5:
#         return


# print(more_than_five(z))

# Задача не возвращает значения после проверки.

##########################

# Задача 4

#

# lower_range = input('Введите нижний предел диапазона ', )
# upper_range = input('Введите верхний предел диапазона ', )
# x = []
# i = []
# def odd(x):
#     if x % 2 != 0:
#         for i in range(lower_range, upper_range):
#             break


# print(odd(x))

# как обходить ошибку
# unsupported operand type(s) for %: 'list' and 'int'

###################################

# Задача 5

# x = []
# r = range(20)
# y = list(reversed(x))
# for i in r:
#     if i % 2 == 0 and i % 4 != 0:
#         x.extend([i])
#
#
# print(y)

###################

# Задача 6
season_number1 = 'Зима'
season_number2 = 'Весна'
season_number3 = 'Лето'
season_number4 = 'Осень'

def month_to_season():
    while True:
        try:
            num = int(input("Введите номер месяца: "))
            if num == 1:
                print('Зима')
            elif num == 5:
                season_number2 == 'Весна'
                return num
            elif num == 6:
                season_number3 == 'Лето'
                return num
            elif num == 9:
                season_number4 == 'Осень'
                return num
            break
        except ValueError:
            print("Ошибка, Повторите ввод")


season = month_to_season()
print(f" y {season} у!")

print(month_to_season())

### не понял как сделать.
