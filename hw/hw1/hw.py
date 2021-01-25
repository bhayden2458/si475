#written by MIDN Sean Moriarty

import math

def sortFunc(f1, f2, f3):
    f1 = int(math.ceil(f1))
    f2 = int(math.ceil(f2))
    f3 = int(math.ceil(f3))

    #determine with if statements all possible orderings of the floats
    if f1 < f2:
        if f1 < f3:
            if f2 < f3:
                return [f1, f2, f3]
            else:
                return [f1, f3, f2]
        else:
            if f3 < f2:
                return [f3, f1, f2]
    else:
        if f1 < f3:
            return [f2, f1, f3]
        else:
            if f3 < f2:
                return [f3, f2, f1]
            else:
                return [f2, f3, f1]

float1 = input("Num 1:")
float2 = input("Num 2:")
float3 = input("Num 3:")

listofnums = sortFunc(float1, float2, float3)
print("The ceilings of those numbers sorted are: ["+str(listofnums[0])+", "+str(listofnums[1])+", "+str(listofnums[2])+"]")
