i = 0
while i == 0:
    D = int(input('Enter Day: '))
    M = int(input('Enter Month: '))
    Y = int(input('Enter Year '))
    print (D, '/', M, '/', Y)
    if D * M == Y:
        print('This is a magic date')
        print('You win')
        i = 1
    else:
        print('This is not a magic date')
