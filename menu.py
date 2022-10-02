import os
import dbfiles

def inputrec() :
    '''Добавление записи в справочник - ввод данных из консоли'''
    #os.system('clear')
    fname = input('Фамилия  : ')
    sname = input('Имя      : ')
    phnum = input('Телефон  : ')
    other = input('Описание : ')
    # Здесь не помешает сделать проверку введенных данных
    return (fname, sname, phnum, other)

def delrec() :
    '''Выбор по номеру записи на удаление'''
    return int(input('Укажите номер удаляемой записи : '))

def searchrec(ls : list) :
    '''Поиск записей по ключу'''
    skey = input('Фрагмент имени/фамилии : ')
    slist = list(filter(lambda x: skey in x, ls))
    return slist

def exportdata(gd : list) :
    '''Экспорт данных в файл'''
    fformat = input('В какой формат экспорт? 1 - csv, 2 - json : ')
    if fformat == '1' :
        fname = input('Укажите имя файла (без .csv) : ') + '.csv'
        dbfiles.exportcsv(fname, gd)
        print(f'В {fname} сохранено {len(gd)} контактов')
        return input('Для продолжения нажмите Enter')
    if fformat == '2' :
        fname = input('Укажите имя файла (без .json) : ') + '.json'
        dbfiles.exportjson(fname, gd)
        print(f'В {fname} сохранено {len(gd)} контактов')
        return input('Для продолжения нажмите Enter')

def importdata() :
    fformat = input('Какой формат импортируемого файла? 1 - csv, 2 - json : ')
    fname = input('Имя файла : ')
    if fformat == '1' :
        return dbfiles.loadcsv(fname)
    if fformat == '2' :
        return dbfiles.importjson(fname)
    
def editrec(gd : list) :
    recn = int(input('Введите номер редактируемой записи :'))
    if not recn in range(1, len(gd) + 1) :
        print('Контакта с таким номером нет, увы...')
        return -1
    editr = list(gd[recn - 1])
    s = input('Фамилия [' + editr[0] + ']: ')
    editr[0] = s if s != '' else editr[0]
    s = input('Имя [' + editr[1] + ']: ')
    editr[1] = s if s != '' else editr[1]
    s = input('Телефон [' + editr[2] + ']: ')
    editr[2] = s if s != '' else editr[2]
    s = input('Описание [' + editr[3] + ']: ')
    editr[3] = s if s != '' else editr[3]    
    gd[recn - 1] = tuple(editr)
    return 0