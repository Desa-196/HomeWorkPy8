from enum import IntEnum

class select_menu(IntEnum):
    VIEW_PHONEBOOK = 1
    SEARCH_BY_NAME = 2
    SEARCH_BY_NUMBER = 3
    ADD_NEW_USER = 4

def show_menu():
    print('Добро пожаловать в телефонный справочник.')
    print('Для дальнейшей работы, выберете один из пунктов меню:')
    print('\t 1. Отобразить все записи')
    print('\t 2. Найти запись по имени')
    print('\t 3. Найти запись по номеру телефона')
    print('\t 4. Добавить новую запись')
    print('\t 5. Сохранить изменения в файл')
    return int(input('Введите пункт меню: '))


def read_csv(filename):
    phonebook_list = []
    with open(filename, "r", encoding="utf-8") as data:
        for line in data:
            phonebook_list.append(line.rstrip().split(','))
    return phonebook_list


def print_result(phone_book):
    print_str = ''
    for line in phone_book:
        for row in line:
           print_str += '{:<20s}'.format(row)
        print_str += '\n'
    print(print_str)

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while(choice != 6):

        if choice == select_menu.VIEW_PHONEBOOK:
            print_result(phone_book)
        '''elif choice == select_menu.SEARCH_BY_NAME:
             name = get_search_name()
             print_result((find_by_name(phone_book, name)))
'''
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

        choice = show_menu()

work_with_phonebook()