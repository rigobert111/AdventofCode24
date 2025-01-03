# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:49 2025

@author: Marboe
"""
import numpy as np
from datetime import datetime

data = np.loadtxt('Input_Real_Day04.txt', dtype=str)

print(data)
count = 0

#checks first X MAS (up left to right), MAS (up right to down left)
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if (data[i][j]=='A' and data[i-1][j+1]=='M' and data[i-1][j-1]=='M' and data[i+1][j-1]=='S' and data[i+1][j+1]=='S'):
            count+=1
            
#checks second X SAM (up left to right), SAM (up right to down left)
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if (data[i][j]=='A' and data[i-1][j+1]=='S' and data[i-1][j-1]=='S' and data[i+1][j-1]=='M' and data[i+1][j+1]=='M'):
            count+=1
            
#checks third X SAM (up left to down right), MAS (up right to down left)
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if (data[i][j]=='A' and data[i-1][j+1]=='M' and data[i-1][j-1]=='S' and data[i+1][j-1]=='S' and data[i+1][j+1]=='M'):
            count+=1
            
#checks fourth X MAS (up left to down right), SAM (up right to down left)
for i in range(1, len(data)-1):
    for j in range(1, len(data[i])-1):
        if (data[i][j]=='A' and data[i-1][j+1]=='S' and data[i-1][j-1]=='M' and data[i+1][j-1]=='M' and data[i+1][j+1]=='S'):
            count+=1

print(count)    