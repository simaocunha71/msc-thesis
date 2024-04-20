"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. 
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
from typing import List
def divisible_by_digits(startnum: int, endnum:int) ->List[int]:
    """
    :type startnum: int
        The smallest number in the given range.
    
    :type endnum: int
        The largest number in the given range.
        
    :rtype: List[int]
        A list of numbers contained in the given range whose digits are all divisible by each other.
    """
    return [ startnum*2**i for i,n in enumerate(str(startnum)) if int(n)%1==0 and n<10 ]+[ endnum-1]*(-1)*(endnum//10 - 1) + [1]
