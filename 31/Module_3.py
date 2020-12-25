

# Сделано только 2 первых задания
# ----------------------------------------------------------
# Задание 1
# Напишите функцию, вычисляющую произведение элементов списка
# целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

print("Task 1")

from random import random
from random import randint

d = int(input("input 1 for use a given list [2, 3, 4, 5] as parameter or 2 to generate a list of N random integers: "))

if d == 1 :
    pro = [2, 3, 4, 5]
    product0 = pro[0]*pro[1]*pro[2]*pro[3]
    print("The list is: ", pro)
    print("The product is: ", product0)

elif d == 2 :
    N = int(input("Enter number of elements in the list:  "))
    # N=15
    def product(pr):
        pro = 1
        for i in range(N):
            pro *= pr[i]
        return pro


    arr = [0] * N
    for i in range(N):
        arr[i] = int(random() * 100)

    b = product(arr)
    print(arr)
    print(b)

else:
        print("you put a wrong value")



# ----------------------------------------------------------

# Задание 2
# Напишите функцию для нахождения минимума в списке целых.
# Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.

print("---------------------------------------------------")
print("Task 2")

from random import random
from random import randint
import random

d = int(input("input 1 for use a given list [2, 3, 4, 5] as parameter or 2 to generate a list of N random integers: "))

if d == 1 :
    def mindef():
        pro = [2, 3, 5, 4]
        print("The list is: ", pro)
        print("The minimal value is: ", min(pro))
        # return mindef()

    mindef()

elif d == 2 :
    N = int(input("Enter number of elements in the list:  "))
    def minvalue():
        list0 = []
        for i in range(N):
            num = random.randint(1,19)
            list0.append(num)
            print("List is: ", list0, "Minimal value is: ", min(list0))
        # return minvalue()

minvalue()

    # arr = [0] * N
    # for i in range(N):
    #     arr[i] = int(random() * 100)
    #
    # b = product(arr)
    # print(arr)
    # print(b)

# else:
#     print("you put a wrong value")



# Задание 3
# Напишите функцию, определяющую количество простых чисел
# в списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.





# Задание 4
# Напишите функцию, удаляющую из списка целых некоторое заданное
# число. Из функции нужно вернуть количество удаленных элементов.
#
# Задание 5
# Напишите функцию, которая получает два списка в качестве
# параметра и возвращает список, содержащий элементы обоих
# списков.
#
# Задание 6
# Напишите функцию, высчитывающую степень каждого элемента
# списка целых. Значение для степени передаётся в качестве
# параметра, список тоже передаётся в качестве параметра.
# Функция возвращает новый список, содержащий полученные
# результаты.
