# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:49 2025

@author: Marboe
"""
import numpy as np
from datetime import datetime

#Einlesen der Druckregeln
with open('Example_Input_Day05.txt', 'r') as file:
    datarules = []
    for line in file:
        if line.strip() == '':
            break
        datarules.append(line.strip())
#print("datarules", datarules)

#Einlesen des zu prüfenden Druck-Datensatzes
with open('Example_Input_Day05.txt', 'r') as file:
    dataset = []
    empty_line_found = False
    for line in file:
        if empty_line_found:
            dataset.append(line.strip().split(','))
        if line.strip() == '':
            empty_line_found = True
print("dataset", dataset)           

#Indizierung der Druckregeln zur Vorbereitung des Prüfalgorithmus (s.u)
parts_rules=[]
for data in datarules: 
    parts_rules.append(data.split('|'))
print("parts_rules", parts_rules)

#Prüfalgorithmus Rückwärtssprüfung (Vorherige Zahlen in Datenreihe untersuchen auf "Danach-Suchwert" laut Regelwerk)
def Prüfalg_Rückwärts(x, i, j):
    a=0
    for rule in range(len(parts_rules)):
        if x == parts_rules[rule][0]:
            for k in range(0, -j,-1):
                if parts_rules[rule][1] == dataset[i][-k]:
                    a=1                
    return a
                    
#Prüfalgorithmus Vorwärtsprüfung
def Prüfalg_Vorwärts(x,i,j): 
    b=0
    for rule in range(len(parts_rules)):
        if x == parts_rules[rule][1]:
            for k in range(j, len(dataset[i]), 1):
                if parts_rules[rule][0] == dataset[i][k]:
                    b=1
    return b
                   
count = 0
for i in range(len(dataset)):
    print("Datenset{}".format(i))
    for j in range(len(dataset[i])): 
        x=dataset[i][j]
        a=Prüfalg_Rückwärts(x, i, j)
        b=Prüfalg_Vorwärts(x,i,j)
        if (a+b >=1):
            break
    if (a+b==0):
        print("J is here:{}".format(j))
        print(dataset[i][int(j/2)])
        count+=int(dataset[i][int(j/2)])

print("Gesamtzähler{}".format(count))
