"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
from math import ceil, sqrt

def count_Primes(num: int):
    """
    Implement a function that checks if n is prime or not based on the sieve of Eratosthenes algorithm. The function should return True if n is prime and False otherwise
    
    Args: num (int) - value to check for primality
        
    Returns: True iff num is a prime number
    """
    primes = [0]*1000
    i = 2
    while i <= sqrt(num):
        if not i in primes:
            primes[i] = 1
            print("prime", i)
        i += 1
    return len([x for x in range(sqrt(num)) if x not in primes]) == 0