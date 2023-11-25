#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    high = scores[0]
    low = scores[0]
    hight = 0
    lowt = 0
    for i in range(len(scores)):
        if scores[i] > high:
                high = scores[i]
                hight += 1
        elif scores[i] < low:
                low = scores[i]
                lowt += 1
    return [hight, lowt]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
