def oibq(n):
    if n >= 90:
        print ("A")
    elif n >= 80:
        print("B")
    elif n >= 70:
        print("C")
    elif n >= 60:
        print("D")
    elif n < 60:
        print("E")


o = int(input('enter score'))
oibq(o)
t = int(input('enter score'))
oibq(t)
tr = int(input('enter score'))
oibq(tr)
f = int(input('enter score'))
oibq(f)
fi = int(input('enter score'))
oibq(fi)
a = ((o+t+tr+f+fi)/5)
print ('You average was ',a)
