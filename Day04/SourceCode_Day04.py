# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:49 2025

@author: Marboe
"""
import numpy as np
from datetime import datetime

data = np.loadtxt('Input_Real_Day04.txt', dtype=str)

count = 0

#checks XMAS in a row
for i in range(len(data)):
    for j in range(len(data[i])-3):
        if (data[i][j]=='X' and data[i][j+1]=='M' and data[i][j+2]=='A' and data[i][j+3]=='S'):
            count+=1

#checks SAMX in a row
for i in range(len(data)):
    for j in range(len(data[i])-3):
        if (data[i][j]=='S' and data[i][j+1]=='A' and data[i][j+2]=='M' and data[i][j+3]=='X'):
            count+=1
            
#checks XMAS in a column
for i in range(len(data)-3): 
    for j in range(len(data[i])):
        if (data[i][j]=='X' and data[i+1][j]=='M' and data[i+2][j]=='A' and data[i+3][j]=='S'):
            count+=1           

#checks SAMX in a column
for i in range(len(data)-3): 
    for j in range(len(data[i])):
        if (data[i][j]=='S' and data[i+1][j]=='A' and data[i+2][j]=='M' and data[i+3][j]=='X'):
            count+=1

#checks XMAS diagonal down right
for i in range(len(data)-3): 
    for j in range(len(data[i])-3):
        if (data[i][j]=='X' and data[i+1][j+1]=='M' and data[i+2][j+2]=='A' and data[i+3][j+3]=='S'):
            count+=1
 
            
#checks SAMX diagonal down right
for i in range(len(data)-3): 
    for j in range(len(data[i])-3):
        if (data[i][j]=='S' and data[i+1][j+1]=='A' and data[i+2][j+2]=='M' and data[i+3][j+3]=='X'):
            count+=1
            
#checks XMAS diagonal down left
for i in range(len(data)-3): 
    for j in range(3, len(data[i])):
        if (data[i][j]=='X' and data[i+1][j-1]=='M' and data[i+2][j-2]=='A' and data[i+3][j-3]=='S'):
            count+=1
            
#checks SAMX diagonal down left
for i in range(len(data)-3): 
    for j in range(3, len(data[i])):
        if (data[i][j]=='S' and data[i+1][j-1]=='A' and data[i+2][j-2]=='M' and data[i+3][j-3]=='X'):
            count+=1
            
print(count)    
            
#Summary of challenges: 
    #E1) Calculated diagonal directions twice (e.g. "down right XMAS" already covers "up left SAMX")
    #E2) Out of bounds in range function/ calculation -> calculate stop value down by -3
    #E3) Worked with negative array positions -> Define start-value in range function
    

