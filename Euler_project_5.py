# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:36:08 2019

@author: aurelio
"""

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

maxNumber = 10


divisivel = list()
for i in range(2,maxNumber+1):
    divisivel.append(list())
    count = 0
    number = i
    for j in range(2,maxNumber+1):
        while(number > 1):
            if number % j == 0:
                number = number/j
                count+=1
            else:
                break
        divisivel[i-2].append(count)
        count = 0

finalCombination = list()
biggerExponent = 0
for i in range(len(divisivel[0])):  
    for j in range(len(divisivel[:][0])): 
        if divisivel[j][i] > biggerExponent:
            biggerExponent = divisivel[j][i]
    finalCombination.append(biggerExponent)
    biggerExponent = 0
    
acumulator = 1
for i in range(len(finalCombination)):
    acumulator = acumulator*(i+2)**finalCombination[i]
    
print(acumulator)