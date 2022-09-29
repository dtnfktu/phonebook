def save_to_file_one_string(lst:list, filename: str, sep : str) :
    '''Записывает в файл кортежи из списка'''
    with open(filename,'w') as f:
        for cortege in lst :
            f.write(sep.join(cortege) + '\r')

def save_to_file_on_strings(lst:list, filename: str) :
    '''Записывает в файл кортежи из списка'''
    with open(filename,'w') as f:
        for cortege in lst :
            f.write('\r'.join(cortege) + '\r\r')

def add_to_file(rec : str, filename : str) :
    '''Добавляет запись в файл'''
    with open(filename,'a') as f:
        f.write(rec + '\r')

def read_from_csvfile(filename : str, separ = ';') :
    '''Считывает справочник из файла и возвращает список кортежей '''
    lst = []
    with open(filename,'r') as f :
        temp_list = f.read().splitlines()

    for abonent in temp_list :
        lst.append(tuple(abonent.split(separ)))

    return lst

def read_from_txtfile(filename : str) :
    '''Считывает справочник из файла и возвращает список кортежей '''
    lst = []
    with open(filename,'r') as f :
        temp_list = f.read().splitlines()

    step = 0
    while step < len(temp_list) :
        lst.append(tuple(temp_list[step:step + 4]))
        step += 5

    return lst







c1 = ('Иванов','Василий','+79831112233','основной')
c2 = ('Петров','Степан','+77051842323','рабочий')
c3 = ('Сидоров','Арнольд','+380923212','корпоративный')
c4 = ('Курачев','Алексей','+43215463212','')