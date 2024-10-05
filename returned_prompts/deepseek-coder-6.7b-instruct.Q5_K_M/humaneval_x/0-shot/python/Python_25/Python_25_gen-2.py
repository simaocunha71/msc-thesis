from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors


# Test cases
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]


Explanation:
The function `factorize(n: int) -> List[int]` takes an integer `n` as an argument and returns a list of integers. The function works by repeatedly dividing `n` by a divisor (starting from 2) until `n` is no longer divisible by the divisor. The divisor is then incremented and the process is repeated until `n` is reduced to 1. The remaining factors are added to the list which is then returned.

This implementation uses the `//` operator to perform integer division, which discards the remainder and returns only the quotient.

The time complexity of this function is O(n), as in the worst-case scenario, the function will iterate through all numbers up to `n`. The space complexity is also O(n), as in the worst-case scenario, all factors will be stored in the list.

This function assumes that the input integer `n` is a positive integer greater than or equal to 2. If `n` is less than 2, the function will return an empty list.
"""

# --------------------- END --------------------- #

# --------------------- START --------------------- #

"""
