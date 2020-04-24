import random
print('Rock paper scissors ')
cpu = random.randint(1,3)
x = 1

while x == 1:
    ch = int(input('1 rock, 2 paper, 3 scissors'))
    if ch == 1:
        print ('you chose rock')
        if cpu == 1:
            print('cpu chose rock')
            print('tie')
            print('\n')
        elif cpu == 2:
            print('cpu chose paper')
            x=2
        elif cpu == 1:
            print('cpu chose scissors')
            x=3
    elif ch == 2:
        print ('you chose paper')
        if cpu == 1:
            print('cpu chose rock')
            x=3
        elif cpu == 2:
            print('cpu chose paper')
            print('tie')
            print('\n')
        elif cpu == 1:
            print('cpu chose scissors')
            x = 2
    elif ch == 3:
        print ('you chose scissors')
        if cpu == 1:
            print('cpu chose rock')
            x=2
        elif cpu == 2:
            print('cpu chose paper')
            x = 3
        elif cpu == 1:
            print('cpu chose scissors')
            print('tie')
            print('\n')

if x == 2:
    print('\n')
    print('you lose')
elif x== 3:
    print('\n')
    print('you win')