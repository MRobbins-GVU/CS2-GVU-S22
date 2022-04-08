# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 18:21:41 2022

@author: mrobbins
"""

def fib(n):
    if n == 0:
        return 0
    
    elif n <= 2:
        return 1
    
    else:
        return fib(n - 1) + fib(n - 2)
    
    
def main():
    # print(fib(6))
    
    fib_list = []
    for i in range(1, 9):
        fib_list.append(fib(i))
    
    print(fib_list)
    
main()