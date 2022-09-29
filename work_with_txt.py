def save_phone_number(book):
    """
    Функция записывает новый номер
    """
    path=r'telephon_book.txt'
    with open(path, 'a', encoding='utf-8') as data:
        data.write(f"{book[0]} : {book[1]} \n")

def look_phone_book():
    """
    Показывает всю телефонную книгу
    """
    data = open(r'telephon_book.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()

def search_view_number(contact):
    """
    Ищет контакт по запросу
    """
    f = open(r'telephon_book.txt', 'r')
    line_new = f.readlines()
    f.close()
    for line in line_new: 
        if line.find(contact) == 0:
            print(line)
    
def del_phone_number(contact):
    """
    Удаляет контакт
    """
    f = open(r'telephon_book.txt', 'r')
    Line_new = f.readlines()
    f.close()
    f = open(r'telephon_book.txt', 'w')
    for line in Line_new: 
        if line.find(contact) == -1:
            f.write(line)
    f.close()