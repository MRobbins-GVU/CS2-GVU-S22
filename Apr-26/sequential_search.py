# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 18:15:36 2022

@author: mrobbins
"""

def seq_search(items, search_term):
    for item in items:
        if item == search_term:
            return True
        
    return False
    
    
def main():
    items = [1, 15, 79, -50, 11]
    search_term = 11
    search_term_2 = 1234567890
    
    print(seq_search(items, search_term))
    
    print(seq_search(items, search_term_2))
    
    
main()