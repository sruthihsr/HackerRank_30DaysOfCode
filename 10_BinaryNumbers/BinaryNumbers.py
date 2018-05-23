#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    counter = 0
    maxi =0;
    while (n > 0) :
        rem = n%2
        if (rem==1):
            counter=counter+1; 
        else:
            counter=0;
        maxi = max(counter, maxi);
        n=int(n/2);
    print(maxi)
