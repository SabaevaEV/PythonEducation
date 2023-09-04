from Sem8 import create
from interface import *
path = "phone_book.txt"
create(path)

enter = 0

while enter !=4:
    enter = interface()
    if enter == 1:
        from Sem8 import add_cont
        stroka = str(input('Введите ФИО и номер телефона через пробел '))
        add_cont(path, stroka)
    elif enter == 2:
        from Sem8 import show_all
        print (show_all(path))
    elif enter == 3:
        from Sem8 import search
        stroka = str(input('Введите Фамилию '))
        search (path,stroka)
print ("Спасибо за работу!")