#############################
# созд список функцию потом в эту функцию параметром список потом проверяется

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

# sum_range(start, end)
# def somefunc(start, end):
#     if start > end:
#         start, end = end, start
#     return sum(range(start,end +1))


# print(somefunc(10,7))

# def more_than_five(func):
#     int(func.sort(key = lambda x: x % 5))
#     return

a = [5,'hi', 'favorite', 8, 4, 1, 101]
def more_than_five(a):
    if a > 5 and -a < -5:
        return


print(int(more_than_five(a)))