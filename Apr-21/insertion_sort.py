# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:49:41 2022

@author: mrobbins
"""

def insertion_sort(items):
    # Keep track of sorted / unsorted
    for i in range(1, len(items)):
        # This is the unsorted item we are currently comparing
        comp_item = items[i]
    
        # Compare first unsorted item 
            # Insert that unsorted item in it's proper place
        # We will stop the while loop when:
            # We reach the end of the sorted list 
            # OR We reach an equal number (put it before) 
            # OR We reach a point where we are greater than a 
                # value but less than the next value
        
        # j is where we are at in the comparison
        j = 0
        right_item = items[j]
        
        # if we make it in the while loop, we are not home yet.
        while comp_item < right_item:
            print("made it!")
            right_item = items[j+1]
            
            j += 1
            
        # After the while, we've found home: j??
        # Insert that unsorted item in it's proper place
        home = "foobar"
        temp = items[home]
        items[home] = comp_item
        
            
            
            
        print("end of while")
        
    # Return the sorted list
    return items
    
    
    
def main():
    
    list1 = [ 2, 7, 5, 1 ]
    print(list1)
    
    sorted_1 = insertion_sort(list1)
    print(sorted_1)
    
    
main()



# Saved code snippets I don't know if we need but I hate deleting
# while comp_item > left_item and comp_item < right_item:
# comp_item == comp_item or 
# left_item = items[j]