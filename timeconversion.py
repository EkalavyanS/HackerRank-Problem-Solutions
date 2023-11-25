#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour, minute, second = map(int, s[:-2].split(':'))
    meridian = s[-2:]  # Extract AM or PM
    
    if meridian == "PM" and hour != 12:
        # If it's PM and not 12 PM, add 12 to the hour
        hour += 12
    elif meridian == "AM" and hour == 12:
        # If it's 12 AM (midnight), set the hour to 0
        hour = 0
    
    # Format the time in 24-hour format
    military_time = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    
    return military_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
1
