import random
Num = random.randint(0,36)
a = (Num % 2)


if Num == 0:
    print("green", Num)
elif Num <= 10:
    if a == 1:
        print("red", Num)
    if a == 0:
        print("black", Num)
elif Num <= 18:
    if a == 1:
        print("black", Num)
    if a == 0:
        print("red", Num)
elif Num <= 28:
    if a == 1:
        print("red", Num)
    if a == 0:
        print("black", Num)
elif Num <= 36:
    if a == 1:
        print("black", Num)
    if a == 0:
        print("red", Num)
