"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с
клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
# lst = []
# temp_el = 0

# def mass_fil(a1, d, n, temp_el): # Мое решение
#     if temp_el<n:
#         lst.append(a1 + temp_el * d)
#         temp_el = temp_el + 1
#         return  mass_fil(a1, d, n, temp_el)

#     print(lst)
        

# mass_fil(int(input('Первый элемент= ')), int(input('Разность= ')), int(input('Количество элементов= ')), temp_el)

a1=int(input('Первый элемент= ')) # Aleksander
d=int(input('Разность= '))
n=int(input('Количество элементов= '))

def arprog(a1, d, n):
    if n==1:
        return [a1]
    
    #res=arprog(a1, d, n-1)
    #return res + [res[-1]+d] 
    return (res := arprog(a1,d,n-1)) + [res[-1]+d]

print(*arprog(a1, d, n))