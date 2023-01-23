import pyAesCrypt
import os


def decryption(file, password):
    """Функция дешифровка файла"""

    # Задаём размер буфера
    buffer_size = 512 * 1024

    # Метод шифрования
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "' дешифрован]")

    # Удаляем исходные файлы
    os.remove(file)


def walking_by_dirs(dir, password):
    """Проходимся по директориям"""

    # Перебираем поддиректории (в указанной директории)
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # Если нашёл файл - дешифруй
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input("Введите пароль для дешифрования: ")
walking_by_dirs("your path", password)
