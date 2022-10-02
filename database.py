import os

def printtable(guide : list, printall = True) :
    '''Вывод справочника телефонов в виде таблицы'''
    from sys import platform # Определяемся в какой системе работаем
    if platform == 'linux' :
        os.system('clear')      # команда для Linux
    else :
        os.system('cls')        # команда для Windows
    i = 1
    print('----------------------------------------------------------------------')
    print('|№ п/п|    Фамилия    |      Имя      |   Телефон   |    Описание    |')
    print('----------------------------------------------------------------------')
    for rec in guide :
        print(f'|{i:3}  |{rec[0]:15}|{rec[1]:15}|{rec[2]:13}|{rec[3]:16}|')
        i += 1
    print('----------------------------------------------------------------------')
    if printall :
        print('1 -добавить, 2 - удалить, 3 - поиск, 4 - изменить, 5 - экспорт, 6 - импорт, 0 - выход')
        return int(input('Выберите действие : '))
    else :
        print('Для продолжения нажмите Enter')
        return input()

def addrec(guide : list, rec : tuple) :
    '''Добавление контакт в справочник'''
    guide.append(rec)

def delrec(guide : list, indx : int) :
    '''Удаление записи по индексу'''
    guide.pop(indx)

def searchrec(guide : list, subs : str) :
    '''Поиск записи(ей) по фрагменту'''
    return list(filter(lambda x: subs in x, guide))