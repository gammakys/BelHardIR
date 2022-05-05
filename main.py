cont = 'Старт'
amount = 0

while cont == 'Старт':
#    if f_num == 'Стоп' or oper =='Стоп' or s_num == 'Стоп':
#        break
#       cont = input('Введите "Старт" если хотите попробовать еще раз; иное чтобы завершить: ')
#    else:
    amount += 1
    f_num = float(input('Введите первое число: '))
#    if f_num == 'Стоп' or oper =='Стоп' or s_num == 'Стоп':
#        break
#    elif:
# даже со сдвигом не хочет работать код
    oper = input("Введите операцию: ")
    s_num = float(input('Введите второе число: '))
    if oper == '+':
        amount += 1
        print((f_num + s_num))
    elif oper == '-':
        amount += 1
        print((f_num - s_num))
    elif oper == '*':
        amount += 1
        print((f_num * s_num))
    elif oper == '/':
        amount += 1
        print(f_num / s_num)
    else:
        print('Ошибка')
    cont = input('Введите "Старт" если хотите попробовать еще раз; иное чтобы завершить: ')
print(f"Количество операций {amount}\2")
# 1 Выполнил
# 2 Нужно спросить как это сделать правильно без деления на два
# 3 не разобрался как правильно использовать try для выполнения пункта 3 дз
# 4 не смог реализовать идею с if break elif


