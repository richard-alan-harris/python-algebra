def dec_to_frac (decimal):
    
    declist = []
    for i in str(decimal):
        declist.append (i)
    del declist[0:2]

    x = len(declist)
    if x == 1:
        dnom = 10
    elif x == 2:
        dnom = 100
    elif x == 3:
        dnom = 1000
    decstr = str(decimal)
    fraction = decstr[2:],'/', dnom
    return fraction

print(dec_to_frac(0.34))