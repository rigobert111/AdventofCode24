# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:49 2025

@author: Marboe
"""

with open('input_data.txt') as file:
    data = file.read()
#print(data)

result = 0

for a in range(1, 999):
    for b in range(1, 999):
        word = "mul({},{})".format(a,b)
        occurence = data.count(word)
        result+=a*b*occurence

print(result)
