# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 18:35:47 2022

@author: mrobbins
"""

import time

def O_n_squared(n):
    
    start = time.time()
    #find all possible pairs of numbers between 1 and n
    # for n = 2
    # (1, 1), (1, 2), (2, 1), (2, 2) 
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                triple = (i, j, k)
            
                # Keeps from printing a gazillion outputs
                if i % 1000 == 0 and j % 1000 == 0 and k % 1000 == 0:
                    print(triple)
                
    
    end = time.time()
    runtime = end - start
    return runtime
    
    
    
def main():
    print(O_n_squared(100))
    print(O_n_squared(1000))
    # print(O_n_squared(10000))
    # print(O_n_squared(10000000))
    
main()