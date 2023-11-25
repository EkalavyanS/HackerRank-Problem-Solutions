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
#[[11, 2, 4], 
# [4, 5, 6], 
# [10, 8, -12]]

def diagonalDifference(arr):
    n = len(arr)
    x = 0
    j=0
    ld = 0
    rd = 0
    while x < n:
        ld += arr[x][x]
        x+=1
    print(x)
    while j < n:
        rd += arr[j][x-1]
        j+=1
        x-=1
    s = abs(rd+ld)
    return abs(ld-rd)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
