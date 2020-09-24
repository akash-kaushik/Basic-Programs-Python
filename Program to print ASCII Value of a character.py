# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:28:46 2020

@author: Akash Kaushik
"""

def user_input():
    
    c = input("Enter the Character:")
    return c

character_user = user_input()

ascii_value = ord(character_user)

print("Ascii value of character ", character_user, " is ", ascii_value)
