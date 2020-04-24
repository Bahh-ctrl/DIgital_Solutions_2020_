wall_size = int(input('What is the size of the wall in sq ft'))
ppg = int(input('orice per gallon'))
time= wall_size*0.0714285714
gp = wall_size*0.00892857143
pc = ppg*gp
lc = time*35
tc = pc+lc
print ('time taken:',time)
print ('Gallons used:',gp)
print ('paint cost:$',pc)
print ('Labour cost:',lc)
print ('Total cost:',tc)