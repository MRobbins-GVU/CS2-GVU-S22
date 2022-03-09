# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:51:20 2022

@author: mrobbins
"""

i = 0
while i < 10:
    i += 1
    print(i)
    
list1 = []
list2 = [1, 2, 3]
while len(list1) < len(list2):
    list1 += [0]
    print(list1)

# This is an infinite loop
# j = 0
# while j < 10:
#     print(j)
