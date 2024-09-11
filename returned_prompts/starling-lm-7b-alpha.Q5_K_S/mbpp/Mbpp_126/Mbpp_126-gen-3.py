"""
def sum_common_divisors(a, b):
    divisors = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            divisors.append(i)
    return sum(divisors)

print(sum_common_divisors(10, 15))
"""

# This solution is inefficient because it checks each number in the range from 1 to min(a, b) to see if it is a divisor of both a and b. A more efficient solution can be derived from the fact that the greatest common divisor of two numbers is the product of the distinct prime factors raised to the smallest power they appear in either number.

# The Euclidean algorithm can be used to find the greatest common divisor of two numbers, and this can be used to find the sum of the common divisors.

# Here is an efficient solution:

def sum_common_divisors(a, b):
    # Find the greatest common divisor of a and b
    while b != 0:
        a, b = b, a % b
    
    # The common divisors are all the divisors of the greatest common divisor
    divisors = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            divisors.append(i)
            if i != a // i:
                divisors.append(a // i)
    return sum(divisors)

print(sum_common_divisors(10, 15))  # Outputs: 6

# This solution is more efficient because it only checks each number up to the square root of the greatest common divisor, instead of up to the smaller of the two input numbers.

# This solution also takes into account that if a number appears as a divisor, then its reciprocal also appears as a divisor, but only once.
"""

# Here's a more efficient solution that uses a mathematical property to find the sum of the common divisors of two numbers:

def sum_common_divisors(a, b):
    #