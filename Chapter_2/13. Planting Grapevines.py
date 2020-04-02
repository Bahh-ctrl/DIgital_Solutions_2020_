e = int(input('the amount of space, in feet, used by an end-post assembly: '))
r = int(input('the length of the row, in feet: '))
s = int(input('the space between vines, in feet: '))
v = r - e*2
v = v/s
print('Number of grape vines that will fit:', v)