a = float(input("A value in meters:  "))

d = int(input("input 1 for dimension in cm or 2 for mm "))

if d == 1 :
    print("The value in cm= ", a*100)

elif d == 2 :
    print("The value in mm= ", a*1000)

else:
        print("you put a wrong value")
