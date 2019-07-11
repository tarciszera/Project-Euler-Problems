# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:35:37 2019

@author: aurelio
"""

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

primes = [2]
lastPrime = 100
index = 0
primeList = [2]
while (index < lastPrime):
    for i in range(len(primeList)):
        