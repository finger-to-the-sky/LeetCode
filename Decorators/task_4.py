# Задача 4
#
# 4.1 Написать декоратор, который бы измерял время работы функции и печатал бы его на экран. 4.2 Доработать декоратор
# таким образом, чтобы в логах было название запускаемой функции помимо времени исполнения. 4.3 Доработать декоратор так,
# чтобы запись лога для функции велась в файл, путь к которому нужно было бы задавать во время декорирования, как параметр.

import time


def file_logs_time(path):
    def time_fiction(func):
        def wrapper(*args, **kwargs):

            start = time.time()
            f = func(*args, **kwargs)
            end = time.time() - start
            print(f'Функция {func} выполнилась за {end}')

            with open(path, 'a', encoding='UTF-8') as file:
                file.write(f'Функция {func} выполнилась за {end}\n')

            return f
        return wrapper
    return time_fiction

@file_logs_time('./logs')
def num(a, b):
    return a + b
print(num(1, 1))