# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:36:25 2019
First challenge euler project
@author: aurelio
"""

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
numero = 600851475143
Maior_primo = 1

while(numero > 1):
    Maior_primo += 1
    while(numero % Maior_primo ==0):
        numero = numero/Maior_primo

print(Maior_primo)