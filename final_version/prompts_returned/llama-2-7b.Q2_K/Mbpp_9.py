"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
import math

def find_Rotations(str):
    """ 
        :param str: String to calculate rotations for.
                     Rotation is defined as number of times a character in a given position can be rotated around the string, without affecting the string value itself.
        """  
    rotations = 0
    for i in range(len(str)):
        c = str[i] # character
        
        if (c >= 'a' and c <= 'z'):
            v1 = (math.pow(2, int(math.log10(abs(c - v))))) - 1
            rotations += v1
    
    return rotations