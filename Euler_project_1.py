# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:36:25 2019
First challenge euler project
@author: aurelio
"""

'''
Make the sum of all 3 and 5 multiples bellow 1000
'''


value = 1000
acumulator = 0
for i in range(1000):
    if (i % 3 == 0) | (i % 5 == 0):
        acumulator += i
        
print(acumulator)