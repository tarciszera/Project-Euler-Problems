# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:08:27 2019

@author: aurelio
"""

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
numberA = 0
numberB = 0
previousPalindricNumber = 0
for i in range(100,1000):
    for j in range(100,1000):
        palindricNumber = i*j
        stringNumber = str(palindricNumber)
        index = 0
        for k in range(len(stringNumber)):
            if stringNumber[k] == stringNumber[len(stringNumber)-1-k]:
                index+=1
                
            if index == len(stringNumber)-1:
                if palindricNumber > previousPalindricNumber:
                    previousPalindricNumber = palindricNumber
                    numberA = i
                    numberB = j  
print(numberA*numberB)