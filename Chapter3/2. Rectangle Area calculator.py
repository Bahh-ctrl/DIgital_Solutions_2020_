l1 = int(input("First rectangle length: "))
w1 = int(input("First rectangle width:"))
l2 = int(input("Second rectangle length: "))
w2 = int(input("Second rectangle width: "))
r1 = (l1*w1)
r2 = (l2 * w2)
if r1 > r2:
    print("The first rectangle was larger")
elif r1 == r2:
    print("Both rectangles were the same size")
else:
    print("The second rectangle was larger")