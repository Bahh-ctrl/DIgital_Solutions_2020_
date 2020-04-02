p = int(input("Pennies: "))
n = int (input("Nickles: "))
d = int(input("Dimes: "))
q = int(input("Quarters: "))

m = (p + n * 5 + d * 10 + 1 * 25)
print (m)
if m > 100:
    print ("Your coins add to ", m - 100, "over $1" )
if m == 100:
    print ("Your coins add to $1" )
if m < 100:
    print ("Your coins add to ", 100 - m, "below $1" )
