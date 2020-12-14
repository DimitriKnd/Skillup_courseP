

a = int(input("Enter 1st number:  "))
b = int(input("Enter 2nd number:  "))
c = int(input("Enter 3rd number:  "))

d = int(input("input 1 to obtain the sum or 2 to obtain the product: "))

if d == 1 :
    print("a+b+c =", a+b+c)
if d == 2:
    print("axbxc =", a*b*c)
if d != 1 and d != 2:
    print("you put a wrong value")

# Instead of 3 if we could use if, elif, else:

# if d == 1 :
#     print("a+b+c =", a+b+c)
# elif d == 2:
#     print("axbxc =", a*b*c)
# else:
#     print("you put a wrong value")