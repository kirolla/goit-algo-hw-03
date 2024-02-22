import argparse
from pathlib import Path
import shutil

# Функція для парсингу аргументів командного рядка
def parse_argv():
    # Створення об'єкта парсера
    parser = argparse.ArgumentParser(description="Копіює файли в папку")
    # Додавання аргументів командного рядка
    parser.add_argument("-s", "--source", type=Path, required=True, help="Папка з файлами")
    parser.add_argument("-o", "--output", type=Path, default="dist", help="Папка для копіювання")
    # Парсинг аргументів командного рядка і повернення результату
    return parser.parse_args()

# Функція для рекурсивного копіювання файлів
def recursive_copy(source, output):
    # Ітеруємося по всім елементам у вихідній директорії
    for item in source.iterdir():
        # Перевіряємо, чи є елемент директорією
        if item.is_dir():
            # Якщо так, рекурсивно викликаємо функцію для цієї директорії
            recursive_copy(item, output)
        else:
            # Якщо елемент є файлом, копіюємо його до відповідної піддиректорії
            # Отримуємо розширення файлу та створюємо шлях до піддиректорії у вихідній директорії
            item_name = item.name.split(".")
            folder = item_name[-1]
            folder = output / folder
            # Створюємо піддиректорію, якщо вона ще не існує
            folder.mkdir(exist_ok=True, parents=True)
            # Копіюємо файл у відповідну піддиректорію
            shutil.copy(item, folder)

# Функція для виконання основного коду
def main():
    try:
        # Парсимо аргументи командного рядка
        args = parse_argv()
        # Викликаємо функцію для рекурсивного копіювання файлів
        recursive_copy(args.source, args.output)
    except OSError:
        # Обробляємо виняток, якщо файл або директорія не може бути прочитаним
        print("File or directory can't be read")

if __name__ == "__main__":
    main()