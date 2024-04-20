"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
from math import sqrt
def count_Primes_nums(input_limit):
    """Counts the nums that are primes for a range of input_limt"""
    count = 0 # Initializing the variable count to zero.
    if type(input_limit) == int: # Testing if the given is an integer or not.
        for i in range(1, sqrt(float(input_limit))+1): # Iterating over the input limit's sqrt and + 1 (to include 0).
            if i % 2 != 0:
                count += 1 # Counting the number of prime numbers.
    return count