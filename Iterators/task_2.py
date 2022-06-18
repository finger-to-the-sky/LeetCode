# Задача 2
#
# Написать генератор, который будет принимать на вход строку и возвращать по запросу последовательно числовое
# представление из таблицы ASCII очередного символа этой строки.


def genenerateASCII(string):
    for i in string:
        yield ord(i)

ne = genenerateASCII('abcd')

print(next(ne))
print(next(ne))





