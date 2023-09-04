from Sem8 import *
from interface import *

while True:
    interface()
    enter = int(input("Выберите действие: "))
    if enter == 1:
        chelovek = str(input('Введите ФИО и номер телефона через пробел '))
        add_contakt(chelovek)
    elif enter == 2:
        show_all()
    elif enter == 3:
        poisk = str(input('Введите данные для поиска '))
        search (poisk)
    elif enter == 4:
        changes = str(input('Введите данные для изменения контакта '))
        change (changes)  
    elif enter == 5:
        deleteEl = str(input('Введите данные для удаления '))
        delete_element (deleteEl)  
    elif enter == 6:
        break
    else:
        print ("Введены неверные данные")
#print ("Спасибо за работу!")