#counter = 0
#while counter < 5:
#   print(f'Счетчик равен: {counter}')
#    counter += 1


#some_list = [1, 2, 3]
#for item in enumerate(some_list):
#    print(f'Элемент  с индексом {item[0]} равен {item[1]}')
#
#some_dict = {1: 100, 2: 200}
#for key, value in some_dict.items():
#    print(f'Элемент с ключем {key} равен {value}')
# функция enumerate показывает при каком индексе какой элемент, а именно
# индекс 0 =  1 и тд

#counter = 0
#while counter < 10:
#    if counter == 8:
#        break
#    print(f'Счётчик равен {counter}')
#    counter += 1
# += увеличивает наше значение counter на 1 каждый раз
# если поставить counter += 2 то будет увеличивать на 2 и тд.

#for i in range(6):
#    if i % 2 == 0:
#        continue
#    print(f'i равно {i}')
# знак % - "кратно"

#for i in range(5):
#    print(f'i равно {i}')
#    break
#else :
#    print('цикл выполнился полностью')


#for i in range(9):
#    print(f'i равно {i}')
#else :
#    print('цикл выполнился полностью')

#some_data = ['раз', 'два']
#for string in some_data:
#    for ch in string:
#        print(ch)
#    print('конец строки')
# циклы могут быть вложены в друг друга и выпоняться последовательно.
# some_data -> это список;
# string, ch -> это все переменные

#def up(string):
#    if isinstance(string, str):
#        return string.upper()
#    else:
#        raise TypeError(f"up RGUMENT MUST BE  ASTRING")

#    try:
#        print (up(1))
#    except TypeError as exc:
#        print (f'Возникла ошибка {exc}')

#####################

# вывести элементы меньше 5
#for a in [1,1,2,3,5,8,13,21,34,55,89]:
#    if a < 5:
#        print(a)
#a=[1,1,2,3,5,8,13,21,34,55,89]
#b = []
#c = []
#for i in a:
#    elif i % 2 == 0:
#        b.append(i)
#    elif:
#        c.append(i)
#print(b)
#нужно чтобы выводило два списка

#a=[1,1,2,3,5,8,13,237,21,34,55,89]
#for i in a:
#    print(i)
#    if i == 237:
#        break

#letters = 'UKsdSDSDSDscAdDFASdu'
#t = ''
#for i in letters:
#    if not i.isupper():
#        t += i
#
#print(t)
# получается




begin = 'Логин'
while begin == 'Логин':
    logins = ['Петрович', 'Иванович', 'Владимирович']
    x = str(input('Введите Логин'))
    for x in logins :
        if x == 'Петрович':
            print(f'Добро пожаловать {x} ')
        elif x == 'Иванович' :
            print(f'Добро пожаловать {x} ')
        elif x == 'Владимирович' :
            print(f'Добро пожаловать {x} ')
        else:
            print('Попробуйте ввести Логин еще раз')
        begin = input('Введите "Логин" если хотите попробовать еще раз; иное чтобы завершить ')
#нужно выяснить где я насрал