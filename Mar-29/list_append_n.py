# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:26:30 2022

@author: mrobbins
"""

import time

# T(2n + 4)
# O ? O(n)
def append_n(n):
    # Add N times to the list using .append()
    start = time.time_ns() / 1000000
    
    list1 = []
    list2 = []
    
    for i in range(n):
        list1.append(i) 
        list2.append(i) 
    
    end = time.time_ns() / 1000000
    
    print("time (ms)", n, " :", end-start)
    
def main():
    append_n(10000)
    append_n(20000)
    append_n(30000)
    
main()