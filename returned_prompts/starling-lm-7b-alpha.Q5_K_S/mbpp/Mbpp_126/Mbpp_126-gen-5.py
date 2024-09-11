def sum_common_divisors(a, b):
    # Initialize result
    res = 0
    # Traverse from 1 to min(a, b)
    for i in range(1, min(a, b) + 1):
        # Check if i is a common divisor of both the numbers
        if (a % i == 0 and b % i == 0):
            # If true, add it to the result
            res += i
    return res

# Testing
assert sum_common_divisors(10, 15) == 6
print("Test passed")




























"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def sum_common_divisors(a, b):
    # Initialize result
    res = 0
    # Traverse from 1 to min(a, b)
    for i in range(1, min(a, b) + 1):
        # Check if i is a common divisor of both the numbers
        if (a % i == 0 and b % i == 0):
            # If true, add it to the result
            res += i
    return res

# Testing
assert sum_common_divisors(10, 15) == 6
print("Test passed")
"""



































"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def sum_common_divisors(a, b):
    # Initialize result
    res = 0
    # Traverse from 1 to min(a, b)
    for i in range