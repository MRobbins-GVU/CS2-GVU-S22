# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:47:55 2022

@author: mrobbins
"""


import time

# T(n+3)
# O ? O(n) 
def concat_n(n):
    # Add N times to the list using concatentation
    start = time.time_ns() / 1000000
    
    list1 = []
    
    for i in range(n):
        list1 = list1 + [i] 
    
    end = time.time_ns() / 1000000
    
    print("time (ms)", n, " :", end-start)
    
def main():
    concat_n(10000)
    concat_n(20000)
    concat_n(30000)
    
main()