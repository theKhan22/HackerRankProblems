#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    max=0
    min=0

    for i in range(5):
        if i<4:
            min+=arr[i]
        if i>0:
            max+=arr[i]

    output=str(min)+" "+str(max)
    print(output)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
