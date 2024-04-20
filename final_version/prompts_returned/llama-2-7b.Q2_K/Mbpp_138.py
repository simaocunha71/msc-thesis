"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
import math

def is_Sum_Of_Powers_Of_Two(n):
    pow = str(n).zfill(36)   # convert the number in string of 36-character long.
    return sum([int(x,2) for x in pow if int(x,2) != 0]) > 1 and (1 << n - 1) == 0
    
# Call is_SumOfPowersOfTwo() function on number 'n'

is_SumOfPowersOfTwo(43)