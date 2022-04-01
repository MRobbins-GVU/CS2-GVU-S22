# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:53:33 2022

@author: mrobbins
"""

class Queue:
    
    def __init__(self):
        self._items = []
        
    def insert(self, item):
        """ Adds to the front of the list """
        self._items = [item] + self._items
        
    def remove(self):
        """ Remove the last item of the list """
        # Grab the last item
        last = self._items[-1] 
        
        # Remove the last item and save the _item list
        self._items = self._items[:-1]
        
        # Return that item we grabbed
        return last
    
    def peek(self):
        """ Returns the item at the front of the Queue """
        return self._items[-1] 
    
    def is_empty(self):
        return len(self._items) == 0
    
    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

def main():
    queue1 = Queue()
    queue1.is_empty()           # True
    
    queue1.insert('Maxx')
    queue1.insert('Wishes')
    queue1.insert('Oreo')
    queue1.insert('Ginger')
    print(queue1)
    
    print(queue1.remove()) 
    queue1.is_empty()           # False
    queue1.size()               # Expect 3
    
    print(queue1.peek())
    
main()




