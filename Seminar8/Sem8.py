# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

def create (path):
    try:
        file = open (path, 'r')
    except IOError:
        print ('Создан новый справочник -> phone_book.txt')
        file = open (path, 'w')
    finally:
        file.close()

def add_cont(file_name, stroka):
    data = open (file_name, 'a')
    data.write(stroka + '\n')
    data.close ()

def show_all (file_name):
    data = open (file_name, 'r')
    for line in data:
        print (line[:-1])
    data.close ()

# add_cont(path, 'cdcjwoiejioc')
# show_all(path)
def search (file_name, stroka):
    a = 0
    data = open (file_name, 'r')
    for line in data:
        if stroka in line:
            print(line)
            a = 123
            break
    if a != 123:
        print ('такого человека нет')
    data.close()






# # Not mine #

# import os.path

# # print('Измените Путь папки чтобы продолжить работу')
# # exit()

# filepath = os.path.join("c:/Users/Ivanlogin888/Desktop/Python/Python_semiar_lectures/Seminar_8_Rabota_s_failami",'file.txt')

# def keep_going():
#     while True:
#         solution = input('Выбирете: STOP или GO -> ').upper()
#         if solution == 'STOP': exit()
#         if solution == 'GO': break

# def zapis(arr_data):
#     if os.path.exists(filepath):
#         with open(filepath,'a',encoding = 'utf-8') as f:
#             for i in arr_data:
#                 f.writelines(i + " ")
#             f.write('\n')
#     else:
#         with open(filepath,'w+',encoding = 'utf-8') as f:
#             for i in arr_data:
#                 f.writelines(i + " ")
#             f.write('\n')

# def read_search(teg):
#     with open(filepath,'r',encoding = 'utf-8') as f:
#         for line in f:
#             if teg in line: print(f'По вашему запросу нашлось: {line}')

                

# while True:
#     n = int(input('Введите количество человек для записи -> '))
#     if n >= 0: break

# while n > 0:
#     zapis(input(f'Введите: Фамилию, Имя, Oтчество, Номер телефона человека -> ').split())
#     n -= 1


# keep_going()
# read_search(input('Введите Имя или Фамилию человека которого вы ищите -> '))
# # keep_going()