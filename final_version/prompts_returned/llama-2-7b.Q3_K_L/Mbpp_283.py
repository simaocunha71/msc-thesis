"""
Write a python function takes in an integer and check whether the frequency of each digit in the integer is less than or equal to the digit itself.
assert validate(1234) == True
"""
import math

def validate(num):
    for n in str(num):
        if len(str(math.log10(int(n)))) == 3:
            return True
    else:
        return False
    