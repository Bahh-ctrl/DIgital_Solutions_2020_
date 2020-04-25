no = int(input('number fo laps run '))

i=0
ol = 0
while i > no:
    i=i+1
    ne = int(input('Lap time'))
    if ne>ol:
        top = ne