# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3

# def array (arr, min, max): # 2 вариант/ через функцию
#    result = [] 
#    for i in range(len(arr)):
#     if arr[i] >= min and arr[i] <= max:
#         result.append(i) 
#     return result

n = int (input ("Введите количество элементов массива: "))
list1 = []
list1 = [int(input ("Введите элементы массива: ")) for i in range (n)]
print (list1)

min, max = int(input ("Введите min диапазонa чисел: ")), int(input ("Введите max диапазонa чисел: "))

result = [] # 1 вариант
for i in range(len(list1)):
    if list1[i] >= min and list1[i] <= max:
        result.append(i)
print (result)
