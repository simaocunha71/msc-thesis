"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""

def difference(n):
    return sum([x ** 2 for x in range(1, n + 1)] - sum([x for x in range(1, n + 1)]))
```