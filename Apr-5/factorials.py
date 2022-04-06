# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 19:09:54 2022

@author: mrobbins
"""

def factorial_while(n):
    """ Calculates factorial using a while loop """
    i = n
    total = 1
    
    while i > 0:
        total = total * i
        i -= 1
        
    return total
    
def factorial_recursive(n):
    """ Calculates factorial recursively """
    # Base case
    if n == 1:
        return 1
    
    # Non-base case
    if n > 1:
        return n * factorial_recursive(n-1)

    
def main():
    print(factorial_while(4))
    print(factorial_recursive(4))
    
main()