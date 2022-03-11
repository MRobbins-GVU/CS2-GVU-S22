# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:10:17 2022

@author: mrobbins
"""


from random import randint

class Die:
    """ A single n-sided die. """
    
    # Initilization function, run when a Die is created
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.value = randint(1, 6)
        
    # Called using .roll() to generate a new random number
    def roll(self):
        self.value = randint(1, 6)
        
    # Used to make print(Die) pretty
    def __str__(self):
        return str(self.value)
    
def main():
    die1 = Die(10) # 10 sided die
    die2 = Die(20) # 20 sided die
    
    for i in range(10):
        die1.roll()
        die2.roll()
        print(die1, die2)
    
main()