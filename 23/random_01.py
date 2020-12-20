
# Home Work 2.3 (LISTS) 20.12.20
# Два списка целых заполняются случайными числами. Необходимо:
# ■ Сформироватьтретийсписок,содержащийэлементы обоих списков;
# ■ Сформироватьтретийсписок,содержащийэлементы обоих списков без повторений;
# ■ Сформироватьтретийсписок,содержащийэлементы общие для двух списков;
# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.


# from random import randint
# import random
# list0 = random.sample(range(0, 19), 10)

from random import randint
import random

number = 9
variation = 20

list0 = []

for i in range(0,number):
     num = random.randint(1,variation)
     list0.append(num)

list1 = []

for j in range(0,number):
     num1 = random.randint(1,variation)
     list1.append(num1)


# list0 = []
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))
# list0.append(randint(0, 19))

# Question: Dima is there is another way to introduce 10 random values
# without typing each time a line?

print("Random creation of two lists")

print("the 1st list is", list0)


# list1 = random.sample(range(0, 19), 10)

# list1 = []
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))
# list1.append(randint(0, 19))

print("the 2nd list is", list1)

print("------------------------------------")

#  Task 1. Representation of the list which include 2 initial lists
# There are 5 methods to obtain 3rd list

# 1st method
mergedlist = list0 +list1

# 2nd method
joinedlist = [*list0, *list1]

# 3rd method
newlist = []
newlist.extend(list0)
newlist.extend(list1)

# 4th method
list2 = []
list2 += (list0 + list1)

# 5th method, but not usefull if we need to rework with initial lists
# for the next tasks

# list.extend(list1)

print("Task 1: Different ways to merge two lists")

print("the merged list is", mergedlist)

print("the joined list is", joinedlist)

print("the newww list is", newlist)

print("the 3rddd list is", list2)

# print(list)

#  Task 2. Representation of the list which include 2 initial lists
# without number repetition

listdr = []
for i in list0:
    if i not in listdr:
         listdr.append(i)

for j in list1:
    if j not in listdr:
        listdr.append(j)

print("-------------------------------------")
print("Task 2: List without repetition ", listdr)
print("-------------------------------------")

# --------------------------------------------------
# Task 4: Same elements in both lists

listsame = []

for kh in list0:
    for mh in list1:
        if kh == mh and kh not in listsame:
            listsame.append(kh)


print("Task 3: List with the same elements in the two lists ", listsame)

# listsamewithout = []
# for mr in listsame:
#     if mr not in listsamewithout:
#          listsamewithout.append(mr)
#
#          print("Task 3: List with the same elements in the two lists without repetition ", listsamewithout)

print("-------------------------------------")

# ----- Task 4: Representation of unique list ------

listunique = []
listunique = list(set(list0 + list1))
# sk = list(listunique)
# print(sk)

print("Task 4: Representation of unique list ", listunique)

# unique_list = []
#
# for item in list and list1:
#     unique_list.append(item)
#
#     print("unique elements", )
#     for item in unique_list:
#      print(item)

# print("the unique list is", listunique)

#----- Task 5 "Visualise max and min values of each list" -------

minmaxlist = []

 # minmaxlist.append(max(list, key = lambda item: item[1]))
minmaxlist.append(max(list0))
minmaxlist.append(max(list1))
minmaxlist.append(min(list0))
minmaxlist.append(min(list1))

print("-------------------------------------")
print("Task 5: List with min and max values", minmaxlist)

print("----------End of the task--------------")

