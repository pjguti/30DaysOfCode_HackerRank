#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.

#os.environ['OUTPUT_PATH'] = "C:/Users/GA/Programacion/30DaysOfCode/results/results.txt"
subresult = 0
def factorial(n):
    if (n > 0):
        #print ("n =",n) #, " / factorial(n-1) =", int(factorial(n-1)))
        #print ("n =", n, " / factorial(n-1) =", int(factorial(n-1)))
        subresult = n * factorial(n-1)
        #print("n otra vez")
        #print ("subresult =", subresult)
        n -= 1
    else:
        subresult = 1
    return subresult

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    #print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
