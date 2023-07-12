#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    start=1
    c=0
    c2=0
    while(start<p):
        start+=2
        c+=1

    end=n
    if n%2==0:
        while(end>p):
            end-=2
            c2+=1
    else:
        while(end>p and end-1>p):
            end-=2
            c2+=1

        
    return (min(c,c2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
