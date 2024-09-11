"""
To solve this, you can follow these steps:

1. Sort the three numbers in ascending order.
2. If the three numbers are equal, the median is the average of the three numbers. Otherwise, the median is the middle number.
3. Return the median as a float.

Here's a Python function that implements these steps:

"""
from fractions import Fraction
def median_numbers(n1, n2, n3):
    # Step 1: Sort the three numbers in ascending order.
    numbers = sorted([n1, n2, n3])

    # Step 2 and 3: Calculate the median.
    if numbers[0] == numbers[1] == numbers[2]:
        # If the numbers are equal, the median is the average of the three numbers.
        median = Fraction(sum(numbers), 3).limit_denominator()
    else:
        # If the numbers are not equal, the median is the middle number.
        median = numbers[1]

    return median

# Test the function.
assert median_numbers(25,55,65) == 55.0
print("All tests passed.")







"""

To solve this problem, you can follow these steps:

1. Sort the three numbers in ascending order.
2. If the three numbers are equal, the median is the average of the three numbers. Otherwise, the median is the middle number.
3. Return the median as a float.

Here's a Python function that implements these steps:

```python
def median_numbers(n1, n2, n3):
    # Step 1: Sort the three numbers in ascending order.
    numbers = sorted([n1, n2, n3])

    # Step 2 and 3: Calculate the median.
    if numbers[0] == numbers[1] == numbers[2]:
        # If the numbers are equal, the median is the average of the three numbers.
        median = Fraction(sum(numbers), 3).limit_denominator()
    else:
        # If the numbers are not equal, the median is the middle number.
       