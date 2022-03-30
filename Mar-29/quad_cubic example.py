# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 17:30:48 2022

@author: mrobbins
"""
import time

def quadratic(n):
    start = time.time()
    for i in range(n):
        for j in range(n):
            pair = (i, j)
    end = time.time()
    print(end - start)

def cubic(n):
    start = time.time()
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                triple = (i, j, k)
                
    end = time.time()
    print(end - start)
    
def main():
    #quadratic(10)
    #cubic(10)
    quadratic(1000)
    cubic(1000)
    
    
main()