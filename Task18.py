'''Задача 18: Требуется найти в массиве A[1..N] 
самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное 
число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X'''
A = [1,3,5,7,8,7,5,9]
x = int(input("Введите число х = "))
i = 0
y = x
n =0
for i in range(len(A)):
    while abs(x-A[i])<y:
        y = abs(x-A[i])
        n = A[i]
print (f"Наименьшая разность = {y} Ближайший к х элемент = {n}") 