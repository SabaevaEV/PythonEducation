# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

# 1 Вариант (ТЗ здорового человека)
# data = {'1': 'S001',
#         '2': 'S002',
#         '3': 'S001',
#         '4': 'S005',
#         '5': 'S005',
#         '6': 'S009',
#         '7': 'S007'}
#
# array = []
#
# for key in data:
#         if data[key] not in array:
#                 array.append(data[key])
#
# print(array)


# data = {'1': 'S001',
#         '2': 'S002',
#         '3': 'S001',
#         '4': 'S005',
#         '5': 'S005',
#         '6': 'S009',
#         '7': 'S007'}
#
# print(set([value for key, value in data.items()]))
#
# print(set(data.values()))

# 2 Вариант (ТЗ курильщика)

# dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": "S005"}, {" V ": "S009"}, {" VIII ": "S007"}]
#
# array = []
#
# # из массива словарей в массив значений (ключей) в словаре
# for i in range(0, len(dict)):
#         a = dict[i]
#         for key in a:
#                 array.append(a[key])
#
# new_array = []
#
# for j in array:
#         if j not in new_array:
#                 new_array.append(j)
#
# print(new_array)


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.


# 1 Вариант строго по тз

# array = [0, -1, 5, 2, 3]
# print(len([array[i] for i in range(1, len(array)) if array[i-1] < array[i]]))
# a = ''
# for i in range(1, len(array)):
#     if array[i - 1] < array[i]:
#         a += ' (' + str(array[i - 1]) + ' < ' + str(array[i]) + ') '
# print(a)


# spisok = [4, 3, 5, 6, 1, 2]
# chislo = [[spisok[i-1], spisok[i]] for i in range(1, len(spisok)) if spisok[i] > spisok[i-1]]
# chislo2 = [print(' (' + str(item[0]) + ' < ' + str(item[1]) + ') ') for item in chislo]

# array = []
# # [0, -1, 5, 2, 3]
#
# while True:
#     n = int(input('Введите длину списка -> '))
#     if n > 0:
#         j = 1
#         while j <= n:
#             array.append(int(input(f'Введите {j} элемент массива -> ')))
#             j += 1
#         break
#
# print(array)
# count = 0
# frst = array[0]
# scnd = array[1]
#
# for i in range(0, len(array)):
#     if frst < scnd:
#         count += 1
#     frst, scnd = scnd, array[i]
#
# print(count)

# 2 ВАРИАНТ (универсальный + вывод значений которые больше)

import random

array_frs = []

while True:
    a = input('Как вы хотите заполнить список. Напишите (вручную или автоматически) -> ')
    if a == 'вручную' or a == 'автоматически':
        break

while True:
    array_len = int(input('Введите длину списка -> '))
    if array_len > 0:
        break

# Заполнение списка
if a == 'вручную':
    i = 1
    while i <= array_len:
        a = int(input(f'Введите {i} элемент списка -> '))
        array_frs.append(a)
        i += 1
if a == 'автоматически':
    while array_len > 0:
        a = random.randint(-20, 20)
        array_frs.append(a)
        array_len -= 1

print(array_frs)
count = 0
res_array = ''


for i in range(1, len(array_frs)):
    frst, scnd = array_frs[i-1], array_frs[i]
    if frst < scnd:
        res_array += ' (' + str(frst) + ' < ' + str(scnd) + ') '
        count += 1


print(count)
print(res_array)