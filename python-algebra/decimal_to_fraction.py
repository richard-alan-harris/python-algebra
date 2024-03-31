dec = input('enter a decimal number between 0 and 0.99')
declist = []
for i in dec:
    declist.append (i)

print(declist)
del declist[0:2]
print(declist)