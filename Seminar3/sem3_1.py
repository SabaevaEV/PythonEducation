from random import randint
# Список/массив

# spisok =[]
# spisok =list ()
# spisok.append / добавление
# spisok.pop / удаление
# spisok.index (3)/ поиск числа

# Словари
# slovar = { 1: "один", 2: "два"}
# slovar [4] = "четыре"
# for item in slovar:
#     print (item, slovar [item])
# for key,value in slovar.items ():  #таким способом выдает и ключ и значение
#     print (key,value)  
# print (slovar.itams())
# print (slovar.values()) # принт значений

# Множества - [хранятся только Уникальные элементы]
# mnoj = set()
# mnoj = {1,2,3,4,5,3} # при выводе множества Повторы выводиться не будут
# mnoj.add (4) / добавление в множество

spisok3 = [randint (0,100) for i in range (10)] # рандомное заполнение, но нужно ОБЯЗАТЕЛЬНО
print (spisok3)                                 #     from random import randint сверху

