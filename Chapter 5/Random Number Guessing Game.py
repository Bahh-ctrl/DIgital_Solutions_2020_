import random
r = random.randint(1,100000)
y= 1
x = 0
while y== 1:
    x=x+1
    g = int(input("Guess"))
    if g == r :
        print('you won in', x, 'rounds')
        y = 0
    elif g>r:
        print ('higher')
    elif r>g:
        print('lower')