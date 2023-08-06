list_1 = []
list_1 = list ()
list_1 = [1,2,5,6]

for i in list_1:
    print (i)

print (len(list_1)) # длина списка/массива

print (list_1[3]) # вывод элемента массива
#если поставить - print (list_1[-1]) - то будет выводиться с конца массива

list_1 =[1,5]
print (list_1)
list_1.append (8) # позволяет добавить элемент массива
print (list_1)


list_1 =[]
for i in range (5):
    list_1.append (i)
    print (list_1)
    
    
# Удаление последнего элемента из списка
list_1 = [12,7,-1,21,0]
print (list_1.pop()) # 0
print (list_1) #[12,7,-1,21]
print (list_1.pop()) # 21
print (list_1) #[12,7,-1]
print (list_1.pop()) # -1
print (list_1) #[12,7]
# Удаление конкретного элемента из списка
list_1 = [12,7,-1,21,0]
print (list_1.pop(0)) # 12

# Добавление элемента на нужную позицию
list_1 = [12,7,-1,21,0]
print (list_1.insert(2,11)) # [12,7,11,-1,21,0]

# Срезы
list_1 = [1,2,3,4,5,6,7,8,9,10]
print (list_1 [0]) #1
print (list_1 [1]) #2
print (list_1 [len (list_1)-1]) #10
print (list_1 [-5]) #6
print (list_1 [:]) #[1,2,3,4,5,6,7,8,9,10]
print (list_1 [:2]) #[1,2]
print (list_1 [len(list_1)-2:]) # [9,10]
print (list_1 [2:9]) #[3,4,5,6,7,8,9]
print (list_1 [6:-18]) #[]
print (list_1 [0:len(list_1):6]) # [1,7]
print (list_1 [::6])# [1,7]

# Кортежи
t = ()
print (type(t))

v = [1,8,9]
print (type(v))
v = tuple (v) # переводим значения в Кортеж
print (type(v))

# a=1
# b=2
# a,b = 1,2

a,b,c = v


t = (1,2,3,4,)
for i in range (len(t)):
    print (i)

# Словари
d = {}
d = dict()
d['q'] = 'qwerty'
print (d)

d['w'] = 'werty'
print (d['q'])

dictionary = {}
dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐

print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента

for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

#Множества
colors = {'red', 'green', 'blue'}
print(colors) # {'red', 'green', 'blue'}
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray') # добавляется значение
print(colors) # {'red', 'green', 'blue','gray'}
colors.remove('red') # удаление значения
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red'
colors.discard('red') # ok  # проверка есть ли значение
print(colors) # {'green', 'blue','gray'}
colors.clear() # { } # удалить все значения списка
print(colors) # set()

q = set () # создание множества 

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8} #копия
u = a.union(b) # u = {1, 2, 3, 5, 8, 13,21} # совмещение множеств
i = a.intersection(b) # i = {8, 2, 5} # пересечение множеств
dl = a.difference(b) # dl = {1, 3} # разность множеств
dr = b.difference(a) # dr = {13, 21} # разность множеств
q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} # сначала пересечение а и б
# потом по порядку а объединяем с б, а потом между полученными множествами определяем разность

# замореженное множество
a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})


# LIST COMPREHENSION Генератор списков

# list_1 = [exp for item in iterable] # простая ситуация - список
# list_1 = [exp for item in iterable (if conditional)] # выборка по заданному условию

#    Создать список чисел от 1 до 100
list_1 = []
for i in range(1, 101):
    list_1.append(i)
print(list_1) # [1, 2, 3,..., 100]

# Эту же функцию можно записать так:
list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]


#2. Добавить условие (только чётные числа)
list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]
# Допустим, вы решили создать пары каждому из чисел (кортежи)
list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,(100, 100)]
#Также можно умножать, делить, прибавлять, вычитать. Например, умножить
# значение на 2.
list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1) # [0, 4, 8, 12, 16]
