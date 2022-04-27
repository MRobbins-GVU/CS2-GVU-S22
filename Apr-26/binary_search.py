# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:34:28 2022

@author: mrobbins
"""


def binary_search(values, item):
    # Sort the list
    values.sort()
    
    # Find the midpoint
    left = 0
    midpoint = len(values) // 2
    right = len(values) - 1
    
    # Explore the left or right half as needed
    while left <= right:
        # we find what we're looking for
        if (item == values[midpoint]):
            print("equal")
            return True
        
        # we know it's impossible for the value to exist
        
        # we need to move left
        elif (item < values[midpoint]):
            print("move left")
            temp = midpoint
            midpoint = (right + left) // 2
            right = temp - 1

        # we need to move right
        elif (item > values[midpoint]):
            print("move right")
            temp = midpoint
            midpoint = (right + left) // 2
            left = temp + 1

    
    return False
    
    
def main():
    list1 = [3, 1, 17, -8]
    sorted_list = [-8, 1, 3, 17]
    val1 = 17
    val2 = 500
    val3 = 5
    
    print(binary_search(list1, val1))
    print(binary_search(list1, val2))
    print(binary_search(list1, val3))
    
    
main()








