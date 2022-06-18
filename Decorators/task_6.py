# Задача 6

# 6.1 Написать декоратор, который будет запрашивать у пользователя пароль при попытке функции осуществить вызов.
# Если введён верный пароль, то функция будет выполнена и вернется результат её работы. Если нет - в консоли появляется
# соответствующее сообщение. 6.2 Параметризовать декоратор таким образом, чтобы можно было задавать индивидуальный пароль
# для каждой декорируемой функции.


def password(ind_passwd):
    def decorator(func):
        def wrapper(*args, **kwargs):

            if input('Введите пароль: ') != ind_passwd:
                print('Ошибка индивидуального пароля!')

            else:
                return func(*args, **kwargs)

        return wrapper
    return decorator




@password('admin')
def plus(a ,b):
    return a + b
print(plus(1 ,2))


@password('user')
def minuse(a , b):
    return a - b
print(minuse(3,1))

