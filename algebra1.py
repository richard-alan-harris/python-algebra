#simultaneous equation
#n1/d1 = n2/d2
#if you have 3 you can work out the 4th



def simequation(n1,d1,n2,d2):
    
    if n2 == 0:
        return (d2 * n1 / d1)
    elif d2 == 0:
        return (n2 * d1 / n1)
    else:
        print('please use n2 or d2 for unknown figure')

print(simequation(10,5,7,0))