from enum import IntEnum

class select_menu(IntEnum):
    VIEW_PHONEBOOK = 1
    SEARCH_BY_NAME = 2
    SEARCH_BY_SURNAME = 3
    SEARCH_BY_NUMBER = 4
    ADD_NEW_USER = 5

def show_menu():
    print('Добро пожаловать в телефонный справочник.')
    print('Для дальнейшей работы, выберете один из пунктов меню:')
    print('\t 1. Отобразить все записи')
    print('\t 2. Найти запись по имени')
    print('\t 3. Найти запись по фамилии')
    print('\t 4. Найти запись по номеру телефона')
    print('\t 5. Добавить новую запись')
    return int(input('Введите пункт меню: '))

def add_user(phone_book, user_data):
    phone_book.append(user_data)

def get_new_user():
    user_data = []
    user_data.append(get_string_from_console('Введите фамилию: '))
    user_data.append(get_string_from_console('Введите имя: '))
    user_data.append(get_string_from_console('Введите номер телефона: '))
    user_data.append(get_string_from_console('Введите описание: '))
    return user_data

def get_string_from_console(text):
    return input(text).strip()

def find_string_in_column(phone_book, find_string, column):
    return [x for x in phone_book if str.upper(x[column]) == str.upper(find_string)]

def read_csv(filename):
    phonebook_list = []
    with open(filename, "r", encoding="utf-8") as data:
        for line in data:
            phonebook_list.append(line.rstrip().split(','))
    return phonebook_list

def write_csv(filename, phone_book):
    with open(filename, "a", encoding="utf-8") as data: 
        print(phone_book)
        data.write(','.join(phone_book) + '\n')

def print_result(phone_book):

    print_str = '\n'
    print_str += '{:<10s}'.format('№')
    print_str += '{:<20s}'.format('Фамилия')
    print_str += '{:<20s}'.format('Имя')
    print_str += '{:<20s}'.format('Номер телефона')
    print_str += '{:<20s}'.format('Описание')
    print_str += '\n-------------------------------------------------------------------------------------------------\n'

    i = 1
    for line in phone_book:
        print_str += '{:<10s}'.format(str(i))
        for row in line:
           print_str += '{:<20s}'.format(row)
        print_str += '\n'
        i += 1
    print(print_str)

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while(choice != 6):

        if choice == select_menu.VIEW_PHONEBOOK:
            print_result(phone_book)
        elif choice == select_menu.SEARCH_BY_NAME:
            name = get_string_from_console('Введите имя для поиска: ')
            print_result(find_string_in_column(phone_book, name, 1))
        
        elif choice == select_menu.SEARCH_BY_SURNAME:
            surname = get_string_from_console('Введите фамилию для поиска: ')
            print_result(find_string_in_column(phone_book, surname, 0))

        elif choice == select_menu.SEARCH_BY_NUMBER:
            number = get_string_from_console('Введите номер телефона для поиска: ')
            print_result(find_string_in_column(phone_book, number, 2))

        elif choice == select_menu.ADD_NEW_USER:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv('phonebook.csv', user_data)

        choice = show_menu()

work_with_phonebook()