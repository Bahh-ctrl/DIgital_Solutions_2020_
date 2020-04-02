i = 0
while i == 0:
    score = int(input('what was your score out of 100?'))
    if score <= 50:
        print('Fail')
        i = 1
    elif score <= 59:
        print('Pass')
        i = 1
    elif score <= 80:
        print('Credit')
        i = 1
    elif score <= 100:
        print('Distinction')
        i = 1
    else:
        print('Error, please try again')
        print('\n')


