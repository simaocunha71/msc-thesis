"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""

def sum_digits(n):
    if n > 0 and n < 10:
        d = str(n) # convert the number to string with '0' as the last digit
        return int(''.join([str(i), str(0-int(d[:i])) for i in range(1, len(d))]))
