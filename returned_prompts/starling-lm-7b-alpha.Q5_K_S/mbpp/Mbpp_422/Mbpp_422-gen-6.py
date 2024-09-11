"""
To solve this problem you need to follow these steps:

1. Create a function named `find_Average_Of_Cube` that takes an integer `n` as a parameter.
2. Calculate the sum of cubes of the first `n` natural numbers using the formula `(n*(n+1)/2)^2`.
3. Divide the sum by `n` to find the average.
4. Return the average.

Here is a Python function that accomplishes this:

```python
def find_Average_Of_Cube(n):
    """Find the average of cubes of the first `n` natural numbers."""
    # Calculate the sum of cubes of the first `n` natural numbers
    sum_cubes = (n*(n+1)/2)**2
    # Divide the sum by `n` to find the average
    average = sum_cubes / n
    # Return the average
    return average
```

To test the function, you can use the `assert` statement to verify if the function gives the correct result for the case `n = 2`:

```python
assert find_Average_Of_Cube(2) == 4.5
```

When you run this code, the `assert` statement will pass and the function will correctly calculate the average of cubes of the first `n` natural numbers.

"""

def find_Average_Of_Cube(n):
    """
    Find the average of cubes of the first n natural numbers.
    """
    # Calculate the sum of cubes of the first n natural numbers
    sum_cubes = (n*(n+1)/2)**2
    # Divide the sum by n to find the average
    average = sum_cubes / n
    # Return the average
    return average

assert find_Average_Of_Cube(2) == 4.5
```

In the provided code, the `find_Average_Of_Cube` function calculates the average of cubes of the first `n` natural numbers using the formula `(n*(n+1)/2)^2` and returns the result. The `assert` statement is used to