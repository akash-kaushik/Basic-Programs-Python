# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:03:38 2020

@author: Akash Kaushik
"""


def user_input():
    
    r = "Wrong"
    
    while r.isdigit() == False:
        r = input("Enter the Radius: ")
        
        if r.isdigit() == False:
            print("Enter the Correct Input!")
            
    return int(r)

r = user_input()

area = 3.14*r*r

print("Area = {}".format(area))   