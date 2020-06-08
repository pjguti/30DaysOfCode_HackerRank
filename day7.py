#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

result = []

for i in range(1,len(arr)+1):
    result.append(arr[-i])

result2 = str(result[0])

for j in range(1,len(result)):
    result2 = result2 + " " + str(result[j])

print(result2)