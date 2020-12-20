
# ДР_2_4   20.12.2020

# Задание 1
# Есть три кортежа целых чисел необходимо найти элементы, которые есть во всех кортежах.

# Задание 2
# Есть три кортежа целых чисел необходимо найти элементы,
# которые уникальны для каждого списка.

# Задание 3
# Есть три кортежа целых чисел необходимо найти элементы,
# которые есть в каждом из кортежей и находятся в каждом из кортежей на той же позиции.


print("-------------------------------")
print("Three tuples of random integers ")

from random import randint
import random

dm = int(input("input 1 to obtain the tuples of 10 elements with 0-4 integers inside or put 2 to choose it manually: "))

if dm == 1:
    number = 9
    variation = 4
if dm == 2:
    number = int(input("Enter the number of elements for the tuples:  "))
    variation = int(input("Enter the possible integers (from 0 to n) n =  "))
if dm != 1 and dm != 2:
    print("you put a wrong value")
    exit()

list0 = []

for i in range(0,number):
     num = random.randint(1,variation)
     list0.append(num)

tuple0=tuple(list0)
print(tuple0)

list1 = []

for i in range(0,number):
     num = random.randint(1,variation)
     list1.append(num)
tuple1 = tuple(list1)

print(tuple1)


list2 = []

for i in range(0,number):
     num = random.randint(1,variation)
     list2.append(num)

tuple2 = tuple(list2)
print(tuple2)

# def convert(list0):
#     return tuple0(i for i in list0)

# tuple0 = (3, 4, 5)

# tuple0 = tuple()
# tuple0 = random.sample(range(0, 12), 10)

# print(tuple(tuple0))

# tuple1 = (3, 4, 5)
# tuple1 = tuple()
# tuple1 = random.sample(range(0, 12), 10)
#
# print(tuple(tuple1))
#
# tuple2 = (3, 4, 5)
# tuple2 = tuple()
# tuple2 = random.sample(range(0, 12), 10)

# print(tuple(tuple2))

print("-------------------------------")

listsame = []

for i in tuple(tuple0):
    for j in tuple(tuple1):
        for k in tuple(tuple2):
          if i == j == k and i not in listsame:
            listsame.append(i)


print("Task 1: The sames values in three tuples", listsame)
print("-------------------------------")

# Task 2. Unique values

listunique0 = []
listunique1 = []
listunique2 = []
listunique = []

listunique0 = list(set(tuple(tuple0)))
listunique1 = list(set(tuple(tuple1)))
listunique2 = list(set(tuple(tuple2)))

listunique = listunique0 + listunique1 + listunique2

print("Task 2: Unique values inside each tuple", listunique0, listunique1, listunique2)
print("Task 2: Unique values inside each tuple together", listunique)


# Task 3. Same elements, same positions

listsupersame = []

for a in tuple(tuple0):
    for b in tuple(tuple1):
        for c in tuple(tuple2):
            if a == b == c and tuple0.index(a)==tuple1.index(b)==tuple2.index(c):
              listsupersame.append(a)

print("-------------------------------")
print("Task 3: Same values in the same positions", listsupersame)

indexsupersame = []
for a in tuple(tuple0):
    for b in tuple(tuple1):
        for c in tuple(tuple2):
            if a == b == c and tuple0.index(a)==tuple1.index(b)==tuple2.index(c):
              indexsupersame.append(tuple0.index(a))

print("Task 3 extra: Indexes for them in order  ", indexsupersame)
print("-------------------------------")

