# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:18:19 2022

@author: mrobbins
"""

class Stack:
    
    def __init__(self):
        self._data = []
        
    def push(self, item):
        """ Add item to the end of the Stack """
        self._data += [item]
        # append also works, we just don't need both
        # self._data.append(item) 
        
    def pop(self):
        """ Removes the last item from the Stack """
        # Grab the last item
        last = self._data[-1] 
        
        # Remove the last item and save the _data list
        self._data = self._data[:-1]
        
        # Return that item we grabbed
        return last
        
    
    def peek(self):
        """ Shows the last item in the Stack, without removing it """
        return self._data[-1] 
        
    def is_empty(self):
        return self._data == []
    
    def size(self):
        return len(self._data)
    
    def __str__(self):
        return str(self._data)
    
def main():
    stack1 = Stack()
    
    stack1.push('Melissa')
    stack1.push('Sean')
    stack1.push('Zelda')
    stack1.push('Midna')
    stack1.push('Impa')
    
    print(stack1)
    
    
main()

