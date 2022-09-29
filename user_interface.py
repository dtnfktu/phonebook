from colorama import *
import check as ch  # здесь заготовка для импорта модуля с проверками


def phone_menu(number) -> int:
    '''
    Вывод в консоль меню телефонной книги. В возврате запускает модуль, где функция принимает число от пользователя, проверяет и возвращает его.
    '''
    print('Выберите действие с телефонной книгой (введите цифру от 1 до 5): \n 1 - Просмотреть все контакты \n 2 - Найти номер по имени \n 3 - Добавить новый контакт \n 4 - Экспортировать базу данных в файл \n 5 - Импортироват базу данных в телефонную книгу')
    return ch.check_numbers(ch.check_empty(number))


def input_search(name) -> str:
    '''
    Подменю для поиска контакта по имени. Пользователь вводит имя, далее проверка и в ней возвращает строку.
    '''
    print('Выберите по какому параметру будет поиск: \n 1 - Имя \n 2 - Номер телефона')
    return ch.check_alpha(ch.check_empty(name))


def search_submenu(number) -> int:
    '''
    Подменю после вызова поиска контакта
    '''
    print('Выберите действия для работы: \n 1 - Удалить контакт \n 2 - Редактировать контакт')
    return ch.check_numbers(ch.check_empty(number))


def print_all(data_list: list) -> None:
    '''
    Вывод всех контактов из телефонной книги
    '''
    print(f'Ваши контакты:')
    for line in data_list:
        print(line)


def print_contact(contact_data: str) -> None:
    '''
    Выводит определенный контакт в консоль, н-р после поиска, или редактирования, или добавления.
    '''
    print(f'Карточка контакта: \n {contact_data}')


def input_new_contact(new_contact: str) -> str:
    '''
    Функция добавляет новые данные, возвращает строку.
    '''
    print('Введите через пробел Имя Фамилия Телефон: ')
    return ch.record_lengh(ch.check_empty(new_contact))


def edit_data(contact_data: str) -> str:
    '''
    Функция перезаписывает новые данные поверх имеющейся записи
    '''
    print('Введите новые данные')
    return ch.record_lengh(ch.check_empty(contact_data))
