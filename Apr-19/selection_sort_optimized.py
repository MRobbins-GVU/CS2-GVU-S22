# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 18:44:30 2022

@author: mrobbins
"""

def selection_sort(items):
    # Go through every entry in items 
    for i in range(len(items)):
        # Assume the first is the largest then compare
        largest_idx = 0
        
        need_swap = False
        
        # Find the largest
        for j in range(len(items) - i):
            if items[largest_idx] < items[j]:
                largest_idx = j
            
            if j < len(items) - 1:
                if items[j] > items[j+1]:
                    need_swap = True
                    
        if need_swap == False:
            print("already sorted!")
            return items
        
        ### Swap the largest with the last unsorted item ###
        # Save what is at the largest index
        temp = items[largest_idx]
        
        # The number of sorted items is i
        # Put the last unsorted item into where the largest was
        items[largest_idx] = items[len(items) - i - 1]
    
        # Put the largest item into the last unsorted position
        items[len(items) - i - 1] = temp
        
        print(i, items)
    
    return items
        
        
    
def main():
    print("\n---List 1 ---")
    list1 = [-1, -2, -3, -4]
    print(list1)
    sorted_list1 = selection_sort(list1)
    print(sorted_list1)
    
    print("\n---List 2 ---")
    list2 = [9, 9, 9, 9, 9, 9]
    print(list2)
    sorted_list2 = selection_sort(list2)
    print(sorted_list2)
       
    print("\n---List 3 ---")
    list3 = [1, 2, 3, 4, 5]
    print(list3)
    sorted_list3 = selection_sort(list3)
    print(sorted_list3) 
    
    print("\n---List 4 ---")
    list4 = [ 14, 2, 3, 11, 5]
    print(list4)
    sorted_list4 = selection_sort(list4)
    print(sorted_list4) 
    
    
    
main()



