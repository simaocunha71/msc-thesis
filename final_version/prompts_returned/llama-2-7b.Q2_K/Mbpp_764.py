"""
Write a python function to count number of digits in a given string.
assert number_ctr('program2bedone') == 1
"""

def number_ctr(str):
    ctr = 0;

    for i in str:
        if ord("0") <= ord("z"[i-1]):
            ctr += 1
    
    return ctr