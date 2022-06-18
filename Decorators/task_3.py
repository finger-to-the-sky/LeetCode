# 3.1 Написать кэширующий декоратор. Суть в том, что если декорируемая функция будет запущена с теми параметрами с
# которыми она уже запускалась - брать результат из кэша и не производить повторное выполнение функции. 3.2 Сделать так,
# чтобы информация в кэше была актуальной не более 10 секунд. Предусмотреть механизм автоматической очистки кэша в
# процессе выполнения функций. 3.3 Параметризовать время кэширования в декораторе.
#
import time


def cash(n):
    def decorator(func):
        ls = []
        def wrapper(*args, **kwargs):
            f = func(*args, **kwargs)

            if f in ls:
                f = ls[ls.index(f)]
            else:
                ls.append(f)

            if time.sleep(n):
                ls.clear()

            return f
        return wrapper
    return decorator


@cash(3)
def num(a ,b):
    return a + b
print(num(1 ,1))

