"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""
import math
def next_Perfect_Square(n):
    i=0 # Initialize counter variable
    s= n # Store initial value for square in the variable 's'
    while (i < s +1):
        if (math.sqrt((2*n)+1) == sqrt ):
            break   # If we find a perfect square, return it and stop execution.
        else:
            i += 1 # Increment our counter by one.
    print(i)   # Print the value of our counter
next_Perfect_Square(25)