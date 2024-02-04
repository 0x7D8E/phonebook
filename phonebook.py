
import os


def add_new_user(name: str, phone: str, filename: str):
    """Добавление нового пользователя"""
    with open(filename, 'r+t', encoding = 'utf-8') as wrtb1:
        lins_count = len(wrtb1.readlines())
        wrtb1.write(f"{lins_count + 1};{name};{phone};\n")


def read_all(filename: str) -> str:
    """Возвращает все содержимое телефонной книги"""
    with open(filename, 'r', encoding = 'utf-8') as data:
        resolt = data.read()
    return resolt


def search_user(data: str, filename: str) -> str:
    """Поиск записи по критерию data"""
    with open(filename, 'r', encoding = 'utf-8') as content:
        text = content.readlines()
        resolt = ([item for item in text if data.lower() in item.lower()])
    return (''.join(resolt)).replace(';', ' ') if resolt else 'Вхождений не найдено'


def check_dir(filename: str):
    """Проверка на существование файла"""
    if filename not in os.listdir():
        with open(filename, 'w', encoding = 'utf-8') as data:
            data.write("")


def copy_data(source_file, dest_file):
    """Копирования данных из одного файла в другой"""
    try:
        with open(source_file, 'r', encoding='utf-8') as file_in:
            with open(dest_file, 'w', encoding='utf-8') as file_out:
                for line in file_in:
                    file_out.write(line)
        print('Текст успешно скопирован в новый файл:', dest_file)
    except FileNotFoundError:
        print('Ошибка: файл не найден!')
    except Exception as e:
        print('Произошла ошибка при копировании текста:', e)


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - копирования данных из одного файла в другой
5 - закончить
"""


DATASOURCE = 'phone.txt'
check_dir(DATASOURCE)


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(DATASOURCE))
        # exit()
    elif mode == 2:
        user = input('Введите имя: ')
        phone = input('Введите номер телефона: ')
        add_new_user(name=user, phone=phone, filename=DATASOURCE)
        # exit()
    elif mode == 3:
        search = input('Введите строку для поиска: ')
        print(search_user(search, DATASOURCE))
        # exit()
    elif mode == 4:
        dest_file = input('Введите имя и расширение нового файла: ')
        copy_data(DATASOURCE, dest_file)
        # exit()
    elif mode == 5:
        print('exit')
        exit()


