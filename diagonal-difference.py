#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    length = len(arr)
    a=0
    b=length-1
    leftDiag=0
    rightDiag=0

    for i in range(length):
        rightDiag+=arr[a][b]
        a+=1
        b-=1
        for j in range(length):
            if i==j:
                leftDiag+=arr[i][j]

    return abs(leftDiag-rightDiag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
