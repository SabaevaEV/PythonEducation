# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет,которые нужно перевернуть
import random

n = int (input (f"Введите количество монет: "))
orel = 0
reshka = 0
print ("'0' если решка '1' если орел")
for i in range (n):
    a = random. randint (0,1)
    if a == 0:
        reshka +=1
    elif a == 1:
        orel +=1
    print (a)
if orel == n or reshka == n:
    print (" Ничего переворачивать не нужно")  
elif orel == reshka:
    print (f"Количество орлов и решек одинаково, нужно перевернуть {orel} монет") 
elif orel > reshka:
    print (f"Нужно перевернуть {reshka} монет")
else: print (f"Нужно перевернуть {orel} монет")