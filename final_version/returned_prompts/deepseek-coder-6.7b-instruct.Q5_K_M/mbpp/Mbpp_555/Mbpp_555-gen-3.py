def difference(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    sum_of_numbers = sum([i for i in range(1, n+1)])
    return sum_of_cubes - sum_of_numbers

print(difference(3))  # Output: 30

Explanation:
The function `difference` takes an integer `n` as an argument. 
It calculates the sum of cubes of the first `n` natural numbers using `sum([i**3 for i in range(1, n+1)])` and the sum of the first `n` natural numbers using `sum([i for i in range(1, n+1)])`.
Finally, it returns the difference between the sum of cubes and the sum of numbers.
"""


def difference(n):
    sum_of_cubes = sum([i**3 for i in range(1, n+1)])
    sum_of_numbers = sum([i for i in range(1, n+1)])
    return sum_of_cubes - sum_of_numbers

print(difference(3))  # Output: 30

Explanation:
The function `difference` takes an integer `n` as an argument. 
It calculates the sum of cubes of the first `n` natural numbers using `sum([i**3 for i in range(1, n+1)])` and the sum of the first `n` natural numbers using `sum([i for i in range(1, n+1)])`.
Finally, it returns the difference between the sum of cubes and the sum of numbers.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Problem 2:**
<jupyter_code>
"""
