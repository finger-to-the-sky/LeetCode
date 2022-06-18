# Задача 2
#
# 2.1 Написать декоратор, который внутри себя выполнял бы функцию и возвращал бы результат её работы в случае успешного
# выполнения. В случае возникновения ошибки во время выполнения функции нужно сделать так, чтобы выполнение функции было
# повторено ещё раз с теми же самыми аргументами, но не более 10 раз. Если после последней попытки функцию так и не
# удастся выполнить успешно, то бросать исключение. 2.2 Параметризовать декоратор таким образом, чтобы количество попыток
# выполнения функции можно было задавать как параметр во время декорирования.
#

def error_check(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            count = n
            while count != 0:
                try:
                    return func(*args, **kwargs)

                except Exception:
                    print(f'Ошибка аргументов функции! {args}')
                    count = count - 1
        return wrapper
    return decorator

@error_check(2)
def num(a ,b):
    return a + b

print(num(1 ,1))
print(num(1, ''))