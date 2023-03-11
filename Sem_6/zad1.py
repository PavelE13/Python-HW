"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с
клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
def mass_fil(a1, d, n, temp_el):
    if temp_el<n:
        lst.append(a1 + temp_el * d)
        temp_el = temp_el + 1
        return  mass_fil(a1, d, n, temp_el)
    print(lst)
        
lst = []
temp_el = 0
mass_fil(int(input('Первый элемент= ')), int(input('Разность= ')), int(input('Количество элементов= ')), temp_el)