kg = int(input("Kilogram amount: "))
qwe = kg * 9.8
if qwe > 500:
    print("This is too heavy")
if qwe < 100:
    print("This is too light")
else:
    print ("This is okay")