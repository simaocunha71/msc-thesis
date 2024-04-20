"""
Write a function to find numbers within a given range from startnum ti endnum where every number is divisible by every digit it contains. 
assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""
from math import sqrt
def divisible_by_digits(startnum, endnum):
    res=[]   # Initialize the result to an empty list. 
    for i in range(i+1): # Looping over every digit from 0 to startnum-1. 
        if i==endnum: break     # Break when we come to endnum, or stop at any number divisible by all digits of the range.  
        modulo = endnum % i    # Modulo is remainder after integer division
        if modulo ==0 : res.append(modulo)      # Append the digit on which this step divides to the result list.
    return res         # Return the result list. 
if __name__=="__main__":
    print divisible_by_digits(1,22)