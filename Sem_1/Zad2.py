"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и 
Сережа вместе?
*Пример:*

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""
a=int(input('Введите общее количество журавликов, целое число: '))
if a>=6 and a%6==0:
    p = s = a // 6
    k = 4 * p
    print("Количество сделанных журавликов: Катя - {} шт., Петя - {} шт., Сережа - {} шт. Done!".format(k,p,s))
else:
    print ('Введенное количество журавликов должно быть кратно 6, иначе условие задачи не выполняетя. Прерывание!')