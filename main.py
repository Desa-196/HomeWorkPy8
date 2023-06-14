from enum import Enum
import os

class select_menu(Enum):
    VIEW_PHONEBOOK = 1
    SEARCH_BY_NAME = 2
    SEARCH_BY_NUMBER = 3
    ADD_NEW_USER = 4

def show_menu():
    os.system('CLS')
    print('Добро пожаловать в телефонный справочник.')
    print('Для дальнейшей работы, выберете один из пунктов меню:')
    print('\t 1. Отобразить все записи')
    print('\t 2. Найти запись по имени')
    print('\t 3. Найти запись по номеру телефона')
    print('\t 4. Добавить новую запись')
    return input('Пункт меню: ')

# def read_csv:

def print_result(phone_book):
    print('Результат')

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while(choice != 6):

        if choice == select_menu.VIEW_PHONEBOOK:
            print_result(phone_book)
        # elif choice == select_menu.SEARCH_BY_NAME:
        #     name = get_search_name()
        #     print(find_by_name(phone_book, name))

        # elif choice == select_menu.SEARCH_BY_NUMBER:
        #     number = get_search_number()
        #     print(find_by_number(phone_book, number))

        # elif choice == select_menu.ADD_NEW_USER:
        #     user_data = get_new_user()
        #     add_user(phone_book, user_data)
        #     write_csv('phonebook.csv', phone_book)

        # elif choice == 5:
        #     file_name = get_file_name()
        #     write_txt(file_name, phone_book)

        choice = show_nemu()

work_with_phonebook()