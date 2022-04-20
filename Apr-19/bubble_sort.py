# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:32:57 2022

@author: mrobbins
"""

def bubble_sort(items): 
    # Run through all the entries in items
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            # Compare the first item to the next 
            if(items[j] > items[j+1]):
                # Swap if needed 
                temp = items[j+1] 
                items[j+1] = items[j]
                items[j] = temp
                
            print(i, j, items)
        
    # Don't compare elements that you know are sorted
    # ^^^ This step is accomplished by subtract i from
    #     the range in j
    
    return items
    
def main():
    # list1 = [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ] 
    # print(list1)
    
    # sorted_list = bubble_sort(list1)
    # print(sorted_list)
    
    
    list2 = [ 0, 1, 2, 3, 4 ] 
    print(list2)
    
    sorted_list_2 = bubble_sort(list2)
    print(sorted_list_2)
    
    
main()




