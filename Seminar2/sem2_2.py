# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# # Защита от дурака
# while True:
#     n = int(input('Введите кол-во дней (от 1 до 100):  -> '))
#     if n <= 100 and n >= 1:
#         break
#
# days = []
# count = 0
# temp = 0
#
# # цикл для заполнения массива данными ср.суточной температуры
# while n > 0:
#     days.append(random.randint(-50, 50))
#     n -= 1
#
# print(days)
#
# # Цикл для подсчета дней с ср.суточной температурой > 0
# for i in range(0,len(days)):
#     if days[i] > 0:
#         temp += 1
#         if temp > count:
#             count = temp
#     else:
#         temp = 0
#
# # Для красоты вывода
# if count == 1 or count % 10 == 1:
#     day = 'день'
# if 1 < count < 5 or 1 < count % 10 < 5:
#     day = 'дня'
# else:
#     day = 'дней'
#
#
# # Вывод
# print(f'Самая длинная оттепель длилась - {count} {day}')

# 2 Вариант
# while True:
#     n = int(input('Введите кол-во дней (от 1 до 100):  -> '))
#     if n <= 100 and n >= 1:
#         break

# temp = 0
# count = 0

# while n > 0:
#     a = int(input('Введите среднесуточную температуру от (-50, 50):  -> '))
#     if a > 0:
#         temp += 1
#         if temp > count:
#             count = temp
#     else:
#         temp = 0
#     n -= 1

# print(count)


# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать самый тяжелый
# арбуз, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input('Введите число арбузов -> '))
#
# watermelons = []
# while n > 0:
#     watermelons.append(random.randint(1,16))
#     n -= 1
#
# print(watermelons)
#
# # max_weight = max(watermelons)
# # min_weight = min(watermelons)
# # print(f'Ваш арбуз весит {max_weight} кг,'
# #       f' a aрбуз для тещи весит {min_weight} кг')
#
# max_weight = watermelons[0]
# min_weight = watermelons[1]
#
# # защита от дурака
# if min_weight > max_weight:
#     min_weight , max_weight = max_weight , min_weight
#
# for i in range(0,len(watermelons)-1):
#     if watermelons[i] > max_weight:
#         max_weight = watermelons[i]
#     if watermelons[i] < min_weight:
#         min_weight = watermelons[i]
#
#
# print(f'Ваш арбуз весит {max_weight} кг,'
#       f' a aрбуз для тещи весит {min_weight} кг')


while True:
    n = int(input('Введите кол-во арбузов  -> '))
    if n > 1:
        break

max_weight = 0
min_weight = 30000


while n > 0:
    temp = int(input(f'Введите вес арбуза {n} -> '))
    if min_weight > temp:
        min_weight = temp
    if max_weight < temp:
        max_weight = temp
    n -= 1


print(f'Ваш арбуз весит {max_weight} кг,'
      f' a aрбуз для тещи весит {min_weight} кг')

# #Разложение числа на простые множители
#
# while True:
#     n = int(input('Введите положительное число -> '))
#     if n >= 1:
#         break
#
# res = []
# temp = 2
#
# while n > 1:
#     if n % temp == 0:
#         res.append(temp)
#         n //= temp
#     else:
#         temp += 1
#
# print(res)


# Вывод всех двухзначных чисел, кратных 5
# print(*range(10,100,5))