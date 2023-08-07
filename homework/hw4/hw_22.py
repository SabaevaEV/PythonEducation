# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input ("Введите количество элементов первого множества: "))
m = int(input ("Введите количество элементов второго множества: "))

mnoj1 = set ()
mnoj2 = set ()

for i in range (n):
    mnoj1.add (int (input (f"Введите {i+1} значение множества 1: ")))
print (mnoj1)
for i in range (m): 
    mnoj2.add (int(input (f"Введите {i+1} значениe множества 2: ")))
print (mnoj2)

mnoj = mnoj1.union(mnoj2) # совмещение множеств
print (sorted(mnoj)) # сортировка