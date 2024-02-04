
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



def copy_text_line_to_file(input_file, output_file):
    """Копирования выбранной строки из одного файла в другой"""
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден. Проверьте правильность имени файла.")
        return

    line_number = int(input("Введите номер строки для копирования: ")) - 1

    if line_number < 0 or line_number >= len(lines):
        print(f"В указанном файле нет строки с номером {line_number + 1}.")
        return

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(lines[line_number])



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
        output_file = input('Введите имя и расширение нового файла: ')
        copy_text_line_to_file(DATASOURCE, output_file)
        # exit()
    elif mode == 5:
        print('exit')
        exit()


