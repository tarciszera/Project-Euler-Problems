# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:36:25 2019
First challenge euler project
@author: aurelio
"""

'''
Make the sum of all 3 and 5 multiples bellow 1000
'''

def getSumBellow(value, number):
    maxMult = value//number + 1
    
    if (((value % number) == 0)):
         maxMult -= 1
    
    acumulation = 0
    for i in range(1,maxMult):
        acumulation += number*i
    
    return acumulation

value = 1000

sumof = getSumBellow(value, 3) + getSumBellow(value, 5)

print(sumof)