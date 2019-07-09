# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:36:25 2019
First challenge euler project
@author: aurelio
"""

'''
Make the sum of all fibonacci even numbers bellow 4 million
'''
import time

startTime = time.time()
currentNumber = 1
acumulator = 0
nextNumber = 2

while(currentNumber < 4e6):
    
    if((currentNumber % 2) == 0):
        sumAc = currentNumber
        acumulator += sumAc
    nextNumber = nextNumber + currentNumber
    currentNumber = nextNumber - currentNumber
    
endTime = time.time()

print(acumulator)
print(endTime - startTime)