# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
# не превосходящие числа N.

n = int (input ("Введите число: "))
x = 2
while x <= n:
    print(x)
    x = x*2