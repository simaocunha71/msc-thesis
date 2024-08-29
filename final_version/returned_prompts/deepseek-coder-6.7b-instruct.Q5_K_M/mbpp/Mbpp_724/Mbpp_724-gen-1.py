"""
Here is a Python solution for the problem:

This program uses two functions. The first function, power_base(base, power), calculates base to the power power. The second function, sum_digits(n), calculates the sum of all digits of a number n. The main function, power_base_sum(base, power), combines these two functions to solve the problem.
"""

def power_base(base, power):
    return base ** power

def sum_digits(n):
    return sum(int(digit) for digit in str(n))

def power_base_sum(base, power):
    return sum_digits(power_base(base, power))

# Test the function
assert power_base_sum(2,100)==115
"""

