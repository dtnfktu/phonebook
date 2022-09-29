from cmath import phase

import phonenumbers
import os

if os.path.exists('testphones.csv') :
    guidelist = phonenumbers.read_from_csvfile('testphones.csv')
else : 
    guidelist = []

os.system('chcp 65001')

def mainmenu():
    '''Выводит в консоль меню и возвращает выбранный пункт'''
    os.system('cls')
    print('Выберите действие :')
    print('1 - Просмотр записей')
    print('2 - Добавление записи')
    print('3 - Экспорт данных')
    print('4 - Импорт данных')
    print('5 - Удалить запись')
    print('6 - Поиск')
    print('0 - Завершить работу')
    key = input()
    return int(key)

def print_guide(guide : list, ent = True) :
    '''Вывод справочника на экран (в консоль)'''
    os.system('cls')
    num = 1
    print('-----------------------------------------------------------')
    print('| № |   Фамилия  |     Имя     | № телефона |  Примечание  |')
    print('-----------------------------------------------------------')
    for rec in guide :
        print(f'|{num:3}|{rec[0]:13}|{rec[1]:12}|{rec[2]:12}|{rec[3]:14}|')
        num += 1
    print('-------------------------------------------------------')
    if ent :
        print('Нажмите Enter для возврата в меню')
        input()

def menu_point1() :
    '''Первый пункт меню - просмотр справочника'''
    print_guide(guidelist)
    
def menu_point2() :
    '''Добавление записи в справочник'''
    sname = input('Фамилия       : ')
    fname = input('Имя           : ')
    phnum = input('№ телефона    : ')
    other = input('Дополнительно : ')
    guidelist.append((sname, fname, phnum, other))
    # rec = sname + ';' + fname + ';' + phnum + ';' + other
    # print('Добавляется запись : ' +  rec)
    # key = input('Сохранить (д/н) ? [Д] :')
    # if key in ('','Д','д','y','Y') :
    #     phonenumbers.add_to_file(rec, 'testphones.csv')
    print('Добавлено в текущий справочник')
    shw = input('Показать? [Д] :')
    if shw in ('','Д', 'Y', 'y','д') :
        print_guide(guidelist)

def menu_point3() :
    '''Экспорт справочника в файл'''
    os.system('cls')
    print('Выберите формат для экспорта :')
    key = input('1 - построчно, 2 - в одну строку, 0 - отмена : ')
    if key == '2':
        separ = input('Укажите символ-разделитель [;] : ')
        separ = ';' if separ == '' else separ
        fname = input('Укажите имя файла [testphonebook.csv] : ')
        fname = 'testphonebook.csv' if fname == '' else fname
        phonenumbers.save_to_file_one_string(guidelist, fname, separ)
        print(f'Готово. Справочник сохранён в файл <{fname}>')
        print('Нажмите Enter для продолжения')
        input()
    if key == '1' :
        fname = input('Укажите имя файла [testphonebook.txt] : ')
        fname = 'testphonebook.txt' if fname == '' else fname
        phonenumbers.save_to_file_on_strings(guidelist, fname)
        print(f'Готово. Справочник сохранён в файл <{fname}>')
        print('Нажмите Enter для продолжения')       
        input()

def menu_point4():
    '''Импорт справочника из файла'''
    os.system('cls')
    fname = input('Укажите имя файла : ')
    if not os.path.exists(fname) :
        print('Указанный файл не найден. Нажмите Enter для продолжения')
        input()
        return
    # Определяем по расширению способ записанной информации
    ext = fname[fname.index('.') + 1:]
    if ext == 'txt':
        k = input('Каждое поле с новой строки. Да? [Д] : ')
        if k in ('','y','Y','д','Д') :
            ftype = 1
    elif ext == 'csv' :
        k = input('Каждая запись в одну строку. Да? [Д] : ')
        if k in ('','y','Y','д','Д') :
            ftype = 2
    else :
        ftype = int(input('Укажите тип файла: 1 - построчный, 2 - в одну строку : '))

    if ftype == 2 :
        sep = input('Укажите символ-разделитель : ')
        guidelist = phonenumbers.read_from_csvfile(fname, sep)
    if ftype == 1 :
        guidelist = phonenumbers.read_from_txtfile(fname)
    print_guide(guidelist)

def menu_point5():
    '''Удаление записи'''
    print_guide(guidelist, False)
    key = int(input('Введите номер удаляемой записи : '))
    if key in range(1,len(guidelist)+1) :
        guidelist.pop(key - 1)
    print_guide(guidelist, False)
    print('Нажмите Enter для продолжения')
    input()

def menu_point6():
    '''Поиск записей по ключу'''
    os.system('cls')
    word = input('Введите часть имени/фамилии/номера :')
    tmplst = []
    for rec in guidelist:
        if word in rec :
            tmplst.append(rec)
    print_guide(tmplst)

while True :
    point = mainmenu()
    if point == 0 :
        break
    if point == 1 :
        menu_point1()
    if point == 2 :
        menu_point2()
    if point == 3 :
        menu_point3()
    if point == 4 :
        menu_point4()
    if point == 5 :
        menu_point5()        
    if point == 6 :
        menu_point6()    

print('Работа завршена...')
