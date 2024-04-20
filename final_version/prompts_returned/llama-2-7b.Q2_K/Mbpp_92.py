"""
Write a function to check whether the given number is undulating or not.
assert is_undulating(1212121) == True
"""
import math

def is_undulating(num):
    if not num % 2:
        return False;
    
    num = (math.pow(10,num-1))/10 #change the number to 10^n format
    temp = num//2                            # divide by two
    while temp > 0:
        if temp % 2 != 0:
            return False;
        temp //= 2;
    return True;

assert is_undulating(1212121) == True
