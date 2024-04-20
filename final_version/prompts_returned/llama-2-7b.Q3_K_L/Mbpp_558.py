"""
Write a python function to find the sum of the per-digit difference between two integers.
assert digit_distance_nums(1,2) == 1
"""
from typing import Optional

def digit_distance_nums(n1: int , n2: int ) -> int :
    total = 0
    number_dict = {}

    for i in range(len(str(n1))):
        digit = str(n1)[i]
        digit_dict = number_dict.setdefault(digit, 0)

        if digit == '9':
            digit_dict += 1

        else:
            digit_dict -= 1

    for j in range(len(str(n2))):
        digit = str(n2)[j]
        digit_dict = number_dict.setdefault(digit, 0)

        if digit == '9':
            digit_dict += 1

        else:
            digit_dict -= 1
        
    for k in range(len(str(n1))):
        digit = str(n1)[k]
        digit_dict = number_dict.setdefault(digit, 0)
        
        if digit == '9':
            digit_dict += 1

        else:
            digit_dict -= 1
    
    for l in range(len(str(n2))):
        digit = str(n2)[l]
        digit_dict = number_dict.setdefault(digit, 0)
        
        if digit == '9':
            digit_dict += 1

        else:
            digit_dict -= 1
    
    for m in range(len(str(n1))):
        digit = str(n1)[m]
        digit_dict = number_dict.setdefault(digit, 0)
        
        if digit == '9':
            digit_dict += 1

        else:
            digit_dict -= 1
    for o in range(len(str(n2))):
        digit = str(n2)[o]
        digit_dict = number_dict.setdefault(digit, 0)
        
        if digit == '9':
            digit_dict += 1

        else:
            digit_dict -= 1
    
    for n in range(len(str(n1))