stpo = int(input('What is the starting population'))
inc = int(input('population growth in %'))
inc = inc/100
da = int(input('days elapsed'))
print('day---population')
print('1   ',stpo)
i=1
while i<da:
    i=i+1
    tda = da+i
    stpo = stpo+stpo*inc
    print (tda, '   ', stpo)