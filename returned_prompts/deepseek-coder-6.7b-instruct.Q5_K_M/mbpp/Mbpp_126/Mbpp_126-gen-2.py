
def sum_of_common_divisors(n1, n2):
    def common_divisors(n):
        return [i for i in range(1, n + 1) if n % i == 0]
    return sum(set(common_divisors(n1)) & set(common_divisors(n2)))

print(sum_of_common_divisors(10, 15))

# Output: 6

Explanation:
The function `common_divisors(n)` is a helper function that finds all the divisors of a number. It does this by iterating over all numbers from 1 to `n` and checking if `n` is divisible by the current number (`n % i == 0`). If it is, it adds the number to the list of divisors.
The main function `sum_of_common_divisors(n1, n2)` then finds the common divisors of `n1` and `n2` by calling `common_divisors(n1)` and `common_divisors(n2)`, and finds their intersection (`set(common_divisors(n1)) & set(common_divisors(n2))`). Finally, it returns the sum of the common divisors.

This works because the intersection of two sets is a set containing only the elements that are in both sets, and the sum of a set of numbers is the sum of their elements.
"""

def sum_of_common_divisors(n1, n2):
    def common_divisors(n):
        return [i for i in range(1, n + 1) if n % i == 0]
    return sum(set(common_divisors(n1)) & set(common_divisors(n2)))

print(sum_of_common_divisors(10, 15))
"""
assert sum_of_common_divisors(10,15) == 6
"""
<jupyter_output>
6
<jupyter_text>
Problem 2:
<jupyter_code>
