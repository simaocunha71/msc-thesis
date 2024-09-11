"""
The area of a tetrahedron can be calculated by the following formula:

area = sqrt(2 + 2 * sqrt(2)) * a^2

where 'a' is the length of each side of the base.
"""
from math import sqrt

def area_tetrahedron(a):
    """Calculate the area of a tetrahedron."""
    return sqrt(2 + 2 * sqrt(2)) * a ** 2

# Test
assert area_tetrahedron(3)==15.588457268119894




"""
Explanation:
The area of a tetrahedron can be calculated by the formula: area = sqrt(2 + 2 * sqrt(2)) * a^2, where 'a' is the length of each side of the base.
"""



"""
Explanation:
The area of a tetrahedron can be calculated by the following formula: area = sqrt(2 + 2 * sqrt(2)) * a^2, where 'a' is the length of each side of the base. The function area_tetrahedron takes a single argument, 'a', and returns the calculated area. The function uses the sqrt and ** operators from the math module to perform the necessary calculations. The assert statement checks if the function returns the expected result for a given input value of 'a'.
"""

# Python3 program to find minimum number of coins
# to make a change of value V

# Returns the minimum number of coins
# of value 1, 5, 10 and 25 needed to
# make a change of value V
def minCoins(coins, V):
    # Initialize result
    res = 0

    # While V is greater than 0
    while (V > 0):
        # Find the largest coin
        # whose value is less or
        # equal to V
        for i in range(len(coins)):
            if (coins[i] <= V):
                # Subtract the value of
                # largest coin from V
                V -= coins[i]
                #