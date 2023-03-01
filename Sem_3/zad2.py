"""
Задача 18. Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит 
натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""

import random
import math

a=int(input('Введите количество элементов в массиве N: '))
my_lst=[random.randint(0,a) for _ in range(a)]
print (*my_lst)
new_lst=[]
x=int(input('введите некоторое число x='))
for i in range(0,a):
    new_lst.append(math.fabs(x-my_lst[i]))
min_el=min(new_lst)
min_ind=new_lst.index(min_el)
print('Ближайшее числу х значение в списке= {}'.format(my_lst[min_ind]))