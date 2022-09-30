from colorama import *

def check_numbers(number:str)->str:
    '''Проверка на цифры (не более 11 цифр, не допускает ввода пустой строки)'''
    while True:
        try:
            n = input(number)
            if int(n)<100000000000:
                return n
            else:
                print(Fore.RED + 'Вы ввели количество цифр больше возможного! '+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно! Это не номер телефона! Вводите только цифры без пробелов!' + Style.RESET_ALL)

def check_alpha(name:str)->str:
    '''Проверка на буквы (не допускает ввода пустой строки)'''
    while True:
        try:
            a = input(name)
            if a.isalpha():
                return a
            else:
                print(Fore.RED + 'Вы ввели символы отличные от букв '+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно!'+ Style.RESET_ALL)

def record_length(length:str)->str:
    '''Проверка длины вводимой строки и тут же проверка на пустую строку'''
    while True:
        try:
            l = input(length)
            if len(l)==0:
                print(Fore.RED + 'Вы ничего не ввели!'+ Style.RESET_ALL)
            elif len(l)<40:
                return l
            else:
                print(Fore.RED + 'Вы ввели слишком много символов '+ Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + 'Неверно! Повторите ввод!'+ Style.RESET_ALL)
