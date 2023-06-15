from enum import IntEnum

class select_menu(IntEnum):
    VIEW_PHONEBOOK = 1
    SEARCH_BY_NAME = 2
    SEARCH_BY_SURNAME = 3
    SEARCH_BY_NUMBER = 4
    ADD_NEW_USER = 5
    DELETE_USER = 6
    EDIT_USER = 7

def show_menu():
    print('Добро пожаловать в телефонный справочник.')
    print('Для дальнейшей работы, выберете один из пунктов меню:')
    print('\t 1. Отобразить все записи')
    print('\t 2. Найти запись по имени')
    print('\t 3. Найти запись по фамилии')
    print('\t 4. Найти запись по номеру телефона')
    print('\t 5. Добавить новую запись')
    print('\t 6. Удалить запись')
    print('\t 7. Изменить запись')
    return int(input('Введите пункт меню, для выхода из программы введите 8: '))

def get_new_user():
    user_data = []
    user_data.append(get_string_from_console('Введите фамилию: '))
    user_data.append(get_string_from_console('Введите имя: '))
    user_data.append(get_string_from_console('Введите номер телефона: '))
    user_data.append(get_string_from_console('Введите описание: '))
    return user_data

#Функция редактирования записи, принимает массив с элементами записи (id, Фамилия, имя ...)
def get_edit_user(user_data):

    surname = get_string_from_console(f'Введите фамилию или оставьте пустым для сохранения старого значения ({user_data[1]}): ')
    if(surname != ''):  user_data[1] = surname
    
    name = get_string_from_console(f'Введите имя или оставьте пустым для сохранения старого значения ({user_data[2]}): ')
    if(name != ''):  user_data[2] = name

    telephone = get_string_from_console(f'Введите номер телефона или оставьте пустым для сохранения старого значения ({user_data[3]}): ')
    if(telephone != ''):  user_data[3] = telephone

    description = get_string_from_console(f'Введите описание или оставьте пустым для сохранения старого значения ({user_data[4]}): ')
    if(description != ''):  user_data[4] = description

    return user_data

def get_string_from_console(text):
    return input(text).strip()

def read_int(text, max, min):
    while(True):
        try:
            #Ввод пытаемся преобразовать в число с плавающей точкой, на случай если ввели не целое число
            readInt = float(input(text))
        #Если при преобразовании в float возникло исключение, выводим ошибку и завершаем иттерацию цикла while
        except:
            print('Введено не число!')
            continue
        #Если попали сюда, значит всё нормально, проверяем равны ли числа типа float и преобразованное в int(откинули дробную часть если она была)
        if  int(readInt) == readInt:
            if readInt > max: print(f'Число должно быть не больше {max}')
            elif readInt < min: print(f'Число должно быть не меньше {min}')
            else: return int(readInt)
        else:
            print('Число должно быть, целым!')

def find_string_in_column(phone_book, find_string, column):
    return [x for x in phone_book if str.upper(x[column]) == str.upper(find_string)]

def read_csv(filename):
    phonebook_list = []
    with open(filename, "r", encoding="utf-8") as data:
        i = 1
        for line in data:
            row = line.rstrip().split(',')
            row.insert(0, str(i))
            phonebook_list.append(row)
            i += 1
    return phonebook_list

def add_csv(filename, new_row_book):
    with open(filename, "a", encoding="utf-8") as data: 
        data.write(','.join(new_row_book) + '\n')

def write_csv(filename, phone_book):
    with open(filename, "w", encoding="utf-8") as data: 
        for line in phone_book:
            data.write(','.join(line[1:]) + '\n')
    

def print_result(phone_book):

    print_str = '\n'
    print_str += '{:<20s}'.format('№ записи')
    print_str += '{:<20s}'.format('Фамилия')
    print_str += '{:<20s}'.format('Имя')
    print_str += '{:<20s}'.format('Номер телефона')
    print_str += '{:<20s}'.format('Описание')
    print_str += '\n-------------------------------------------------------------------------------------------------\n'

    for line in phone_book:
        for row in line:
           print_str += '{:<20s}'.format(row)
        print_str += '\n'
    print(print_str)

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv('phonebook.csv')

    while(choice != 8):

        if choice == select_menu.VIEW_PHONEBOOK:
            print_result(phone_book)
        elif choice == select_menu.SEARCH_BY_NAME:
            name = get_string_from_console('Введите имя для поиска: ')
            print_result(find_string_in_column(phone_book, name, 2))
        
        elif choice == select_menu.SEARCH_BY_SURNAME:
            surname = get_string_from_console('Введите фамилию для поиска: ')
            print_result(find_string_in_column(phone_book, surname, 1))

        elif choice == select_menu.SEARCH_BY_NUMBER:
            number = get_string_from_console('Введите номер телефона для поиска: ')
            print_result(find_string_in_column(phone_book, number, 3))

        elif choice == select_menu.ADD_NEW_USER:
            user_data = get_new_user()
            add_csv('phonebook.csv', user_data)
            phone_book = read_csv('phonebook.csv')

        elif choice == select_menu.DELETE_USER:
            index = read_int('Введите номер записи для удаления: ', len(phone_book), 1)
            write_csv('phonebook.csv', [i for i in phone_book if i[0] != index])
            phone_book = read_csv('phonebook.csv')

        elif choice == select_menu.EDIT_USER:
            index = read_int('Введите номер записи для редактирования: ', len(phone_book), 1)
            phone_book[int(index) - 1] = get_edit_user(phone_book[int(index) - 1])
            write_csv('phonebook.csv', phone_book)
            phone_book = read_csv('phonebook.csv')

        choice = show_menu()

work_with_phonebook()