peo = int(input("People attending: "))
per = int(input("Hot dogs per-person: "))

t = peo * per
HDP = t // 10
HDR = t % 10
BP = t // 8
BR = t % 8

print ("Required Hotdogs packs:", HDP)
print("Bun Packets required", BP)
print ("Hot dogs left over", HDR)
print ("Buns leftover", BR)
