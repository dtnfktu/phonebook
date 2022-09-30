import init_data as id
import view
import work_with_txt

def book():
    while True:
        print('Список команд: \n 1 - добавить контакт \n 2 - удалить контакт \n 3 - посмотреть список контактов \n 4 - найти номер по имени \n 5 - завершить работу \n')
        command = int(input('Введите номер команды: '))
        if command == 1:
            a = view.get_name()
            b = view.get_number()
            id.phone_number(a, b)
            book_new = id.get_data()
            work_with_txt.save_phone_number(book_new)
            print('Данные сохранены \n')                
        elif command == 2:
            x = view.search_contact()
            work_with_txt.del_phone_number(x)
            print('Данные удалены \n')  
        elif command == 3:
            print('Телефонная книга: \n')
            work_with_txt.look_phone_book()
        elif command == 4:
            x = view.search_contact()
            print('Данные по вашему запросу: \n')
            work_with_txt.search_view_number(x)
        elif command == 5:
            print('Работа завершена')
            break
        else:
            print('Ошибка')