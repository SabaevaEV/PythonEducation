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

def add_contakt(chelovek):
    data = open ('phone_book.txt', 'a', encoding='utf-8')
    data.writelines(chelovek)
    data.writelines('\n')
    data.close ()

def show_all ():
    data = open ('phone_book.txt', 'r', encoding='utf-8')
    for line in data:
        print (line[:-1])
    data.close ()

def search (poisk):
    with  open ('phone_book.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if poisk in line:
                print(line)
                break
        else:
           print ('Такого нет')


# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def change(changes):
    with open ('phone_book.txt', 'r+', encoding ='utf-8') as data:
        change_data=data.readlines()
        with open('phone_book.txt', 'w+', encoding='utf-8') as data:

            for line in change_data:
                if changes in line:
                    data.write(input('Введите новые данные: '))
                    data.write('\n')
                else:
                    data.write(line)


def delete_element(deletEl):
    with open('phone_book.txt', 'r', encoding='utf-8') as data:
        del_data = data.readlines()
    with open('phone_book.txt', 'w+', encoding='utf-8') as data:
        for line in del_data:
            if deletEl not in line:
                data.write(line)
