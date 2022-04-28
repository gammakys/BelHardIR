cont = 'Старт'

while cont == 'Старт':
    f_num =  float(input('Введите первое число'))
    oper = input("Введите операцию")
    s_num = float(input('Введите второе число'))
    if oper == '+':
        print(number_to_words(f_num + s_num))
    elif oper == '-':
        print(number_to_words(f_num - s_num))
    elif oper == '*':
        print(number_to_words(f_num * s_num))
    elif oper == '/':
        print(number_to_words(number_to_words(f_num / s_num)))
    else:
        print('Ошибка')
    cont = input('Введите "Старт" если хотите попробовать еще раз; иное чтобы завершить')






