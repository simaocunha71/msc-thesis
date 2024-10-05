

def largest_divisor(n: int) -> int:
    i = n - 1
    while i > 0:
        if n % i == 0:
            return i
        i -= 1
    return None


print(largest_divisor(15))


"""
This function works by starting at n - 1 and going down to 1. For each number, it checks if n is divisible by that number (i.e., if n modulo that number is equal to zero). If it is, that number is the largest divisor of n, so it's returned.

The function stops once it has checked all numbers from n - 1 down to 1, because if n is not divisible by any number in that range, then n itself is the largest divisor.
"""

# Code:

