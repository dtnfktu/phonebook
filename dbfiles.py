import json
import datetime
import os

def loadcsv(fname : str) :
    '''Загрузка справочника из csv-файла'''
    outlist = []
    with open(fname, 'r', ) as fcsv :
        tmpread = fcsv.read().splitlines()
        for line in tmpread :
            outlist.append(tuple(line.split(';')))
    return outlist

def exportcsv(fname: str, gd : list) :
    '''Записывет список в csv-файл'''
    with open(fname, 'w') as recfile :
        for element in gd :
            recfile.write(';'.join(element) + '\r')

def exportjson(fname : str, gd : list) :
    '''Записывет список в json-файл'''
    # Сначала формируем словарь
    phonebook = {}
    counter = 1
    for contact in gd :
        fcount = 1
        cortege = {}
        for field in contact :
            cortege['f'+str(fcount)] = field
            fcount += 1
             
        phonebook['rec'+str(counter)] = cortege
        counter += 1
    # Теперь записываем всё в json
    with open(fname,'w') as recfile :
        json.dump(phonebook, recfile)

def importcsv(fname : str) :
    '''Импорт контактов из указанного csv-файла'''
    lst = []
    with open(fname,'r') as readfile :
        temp_list = readfile.read().splitlines()
    for abonent in temp_list :
        lst.append(tuple(abonent.split(';')))
    return lst

def importjson(fname : str) :
    '''Импорт контактов из указанного JSON-файла'''
    lst = []
    # Читаем из json
    with open(fname,'r') as readfile :
        phonebook = json.load(readfile,)
    tmplst = phonebook.values()
    
    for contact in tmplst :
        lst.append(tuple(contact.values()))

    return lst
   
def makebackup() :
    '''Создаёт backup файла phonebook.csv'''
    now = str(datetime.datetime.now())
    now = now[:now.find('.')]
    now = now.replace('-','').replace(':','').replace(' ','_')
    if os.path.exists('phonebook.csv') :
        bckp = loadcsv('phonebook.csv')
        exportcsv(now + '.backup',bckp)

