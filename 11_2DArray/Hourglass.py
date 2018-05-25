#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))
    mat = [[0 for x in range(6)] for y in range(6)] 
    for val in arr:
        for i in range(6):
          for j in range(6):
                mat[i][j]=val
    maxSum = -63
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            hourglass = top + mid + bottom
            if hourglass > maxSum:
                maxSum = hourglass
     
                
    print(maxSum)
