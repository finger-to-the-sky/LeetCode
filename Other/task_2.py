# Медиана двух отсортированных массивов.

class Solution:
    def __init__(self, ls_1, ls_2):
        self.ls_1 = ls_1
        self.ls_2 = ls_2


    @staticmethod
    def MedianFind(list_1, list_2):
        result = sorted(list_1 + list_2)
        l = len(result)

        if len(result) % 2 == 0:

            return result[l // 2]
        else:

            return (result[l // 2] + result[(l // 2) + 1]) / 2

    # Решил сделать медиану через статикметод и чтобы не стирать конструктор, хочу дополнить класс.
    # Сделаем метод, который будет находить уникальные элементы из всех, что есть в двух списках.

    def Difference(self):
        set_1 = set(self.ls_1)
        set_2 = set(self.ls_2)
        print('Нахожу уникальные элементы из ваших списков...')
        return list(set_1 ^ set_2)

list_1 = [1, 2, 5, 7, 8]
list_2 = [1, 4, 5]

print(Solution.MedianFind(list_1, list_2))

s = Solution(list_1, list_2)
print(s.Difference())