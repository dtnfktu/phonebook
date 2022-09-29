

def check_numbers(number:str)->str:
    '''Проверка на цифры (не более 11 цифр, не допускает ввода пустой строки)'''
    while True:
        try:
            n = input(number)
            if int(n)<100000000000:
                return n
            else:
                print('Вы ввели количество цифр больше возможного! ')
        except ValueError:
            print('Неверно! Это не номер телефона! Вводите только цифры без пробелов!')

def check_alpha(name:str)->str:
    '''Проверка на буквы (не допускает ввода пустой строки)'''
    while True:
        try:
            a = input(name)
            if a.isalpha():
                return a
            else:
                print('Вы ввели символы отличные от букв ')
        except ValueError:
            print('Неверно!')

def record_length(length:str)->str:
    '''Проверка длины вводимой строки и тут же проверка на пустую строку'''
    while True:
        try:
            l = input(length)
            if len(l)==0:
                print('Вы ничего не ввели!')
            elif len(l)<40:
                return l
            else:
                print('Вы ввели слишком много символов ')
        except ValueError:
            print('Неверно! Повторите ввод!')
