"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций 
допускаются только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2
4
""" 
def sum_1(a, b):
    if b > 0:
        return sum_1(a + 1, b - 1)
    return a

print(sum_1 (int(input('Введите a: ')),b=int(input('Введите b: '))))