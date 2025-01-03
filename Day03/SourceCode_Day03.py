# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:49 2025

@author: VW1WBMY
"""
import re 
from datetime import datetime

with open('C:/Users/VW1WBMY/AdventofCode/Day03/input_data_Day03.txt') as file:
    data = file.read()
#print(data)

result = 0

dtbefore = datetime.now()

#following for part number 1
for a in range(1, 999):
    for b in range(1, 999):
        word = "mul({},{})".format(a,b)
        occurence = data.count(word)
        result+=a*b*occurence

print(result)
dtafter = datetime.now()

diff = dtafter - dtbefore   
print(diff.total_seconds())

#Approach for second task of day 4
# =============================================================================
# key = "mul\(\d+,\d+\)"
# result1 = re.findall(key, data)
# print(result1)
# 
# for i in result1: 
#     a, b = nums(i)
#     count+=a*b
#     
# =============================================================================
    