#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new_str = ""
    flag_upper = True
    for char in s:
        if char == " ":
            new_str += char
            flag_upper = True
        elif flag_upper == True:
            new_str += char.upper()
            flag_upper = False
        else:
            new_str += char
    
    return new_str;
            
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
