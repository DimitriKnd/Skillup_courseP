
# HomeWork 2.4 DICTIONARY  20/12/20
# Задание 1
# Создайте программу, хранящую информацию о вели- ких баскетболистах.
# Нужно хранить ФИО баскетболиста и его рост.
# Требуется реализовать возможность добавления, удаления, поиска, замены данных.
# Используйте словарь для хранения информации.

basket = {
    'Gheorghe Muresan': 231,
    'Manute Bol': 231,
'Slavko Vranes' : 229,
    'Shawn Bradley': 229,
'Yao Ming' : 229,
'Chuck Nevitt' : 226
}

# print(basket['Manute Bol'])
#
# basket['X Y'] = 225
# basket['X Z'] = 224
# print(basket)
#
# del basket['X Z']
# print(basket)


d = int(input("input 1 to introduce new player or 2 to delete the player: "))

if d == 1 :
    a = str(input("Enter the name of player:  "))
    b = int(input("Enter his heigh in cm  "))
    basket[a] = b
if d == 2:
    c = str(input("Enter the name of player:  "))
    del basket[c]
if d != 1 and d != 2:
    print("you put a wrong value")

print(basket)