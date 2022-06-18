# Задача 1
#
# 1.1 Написать класс "Тумбочка", у которой определить поле items, который представлял бы собой список. Реализовать метод
# add_item, который на вход будет принимать произвольный объект и добавлять к списку items. Сделать так, чтобы объект
# класса "тумбочка" был итерируемым: перебор должен осуществляться точно также, как если бы мы итерировались по списку
# items. 1.2 Написать кастомный итератор для тумбочки и реализовать в нём метод to_start, который возвращал бы перебор
# элементов к началу, метод to_custom, который бы ставил курсор перебора на определенный элемент в списке по индексу.


class CustomIterator:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.count = 0

    def to_start(self):
        self.count = 0

    def to_custom(self, coursor):
        max_index = len(self.iter_obj) - 1

        if coursor < 0 or n > max_index:
            raise IndexError
        self.count = n

    def __next__(self):

        while True:

            if self.count < len(self.iter_obj):
                obj = self.iter_obj[self.count]
                self.count += 1
                return obj
            raise StopIteration

class Nightstand:
    def __init__(self, items, obj):
        self.items = items
        self.obj = obj

    def add_items(self):
        self.items.append(self.obj)
        return self.items

    def __iter__(self):
        iteration = CustomIterator(self.items)
        return iteration

my_list = [1, 2, 3, 4]
n = Nightstand(my_list, 5)

print(n.add_items())

for i in n:
    print(i)
