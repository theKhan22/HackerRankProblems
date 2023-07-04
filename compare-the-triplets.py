

import math
import os
import random
import re
import sys



def compareTriplets(a, b):
    c1=0
    c2=0
    for i in range(3):
        if a[i]>b[i]:
            c1+=1
        elif a[i]<b[i]:
            c2+=1
    return [c1,c2]            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
