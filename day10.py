#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

binary = bin(n)
print(binary)
binary2 = binary[2:]
#cadenas = binary.split("0")
print(binary2)

ones = 0
maxOnes = 0

for i in range(len(binary2)):
    print("binary[",i,"] =",binary2[i])
    if (binary2[i]) == "1" :
        print("binary one")
        ones = ones + 1
        print("ones =", ones)
        if (ones > maxOnes):
            maxOnes = ones
            print("maxOnes =",maxOnes)
    else:
        print("binary zero")
        ones = 0

print("maxOnes =", maxOnes)
