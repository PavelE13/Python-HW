"""
Задача 16.Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""
import random

count = 0
n = int(input('Введите количество элементов в массиве N: '))
my_lst = [random.randint(0, n) for _ in range(n)]
print(*my_lst)
x = int(input('введите некоторое число x='))
for i in range(n):
    if my_lst[i] == x:
        count += 1
print(f'число {x} встречается в массиве {count} раз(а)!')