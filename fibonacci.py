# -*- coding: utf-8 -*-
"""
Fibonacci number recursive function script

Consult https://en.wikipedia.org/wiki/Fibonacci_number

Created on Fri Feb  1 11:35:57 2019

@author: shakes
"""

def fibonacci(n):
    '''
    Recursive fibonacci function.
    Compute the Fibonacci number for a given n.
    '''
    #base case
    if n == 0 or n == 1:
        return n
    
    #recursive call
    return fibonacci(n - 2) + fibonacci (n - 1)

print("F(5):", fibonacci(5)) #should be 5
print("F(10):", fibonacci(10)) #should be 55
