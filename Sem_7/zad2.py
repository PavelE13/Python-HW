"""
Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны
быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая
операция, у которой ровно два аргумента, как, например, у операции умножения.

Ввод:
`print_operation_table(lambda x, y: x * y)` 
Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""
x = num_rows = int(input('Введите количество рядов num_rows: '))
y = num_columns = int(input('Введите количество рядов num_columns: '))
operation = lambda x, y: x * y

# def print_operation_table(f, arg1, arg2):
#     for x in range(1,arg1+1):
#         table=[]
#         for y in range(1,arg2+1):
#             table.append(f(x,y))
#         print(*table, sep = '  \t')
        
def print_operation_table(f, arg1, arg2):
    table = map(lambda x: map (lambda y: f(x,y), range (1, arg2 + 1)), range(1,arg1+1))
    print(*table, sep = '  \t')

print_operation_table(operation, num_rows, num_columns)

#def print_operation_table(f, arg1, arg2):
#    for row in range(1, num_rows + 1):  
#       print(*map(f, row[]*num_columns, range(1, num_columns + 1)), sep = '  \t')

#print_operation_table(lambda x,y: x*y, x ,y)