from math import sqrt


def length(parametre1: list, parametre2: list) -> int:
    return sqrt(((parametre1[0]-parametre2[0])**2)+((parametre1[1]-parametre2[1])**2)+((parametre1[2]-parametre2[2])**2))


print(length([1,2,3], [2,3,4]))

def area(parametre1 : list, parametre2 : list, parametre3: list, parametre4: list) :
    if parametre1[0]!= parametre2[0] :
        a=parametre1[0]-parametre2[0]
    else:
        a=parametre1[0]-parametre3[0]
    if parametre1[1]!= parametre2[1] :
        b=parametre1[1]-parametre2[1]
    else:
        b=parametre1[1]-parametre3[1]
    return abs(a*b)

print(area([6,0],[2,0],[6,5],[2,5]))











