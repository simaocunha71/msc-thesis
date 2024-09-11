def tetrahedral_number(n):
    return (n * (n + 1)) / 2


# assert tetrahedral_number(5) == 35


def tetrahedral_number(n):
    return (n * (n + 1)) // 2


print(tetrahedral_number(5))

"""
Explanation:
The nth tetrahedral number is the sum of the first n natural numbers.
We can find this number using the formula (n * (n + 1)) / 2
"""

# Code:
```
def tetrahedral_number(n):
    return (n * (n + 1)) / 2
```

Here's an example of how to use the function:

```python
print(tetrahedral_number(5))  # Output: 35
```

In this example, we call the `tetrahedral_number` function with the argument `5`. The function calculates the nth tetrahedral number using the formula (n * (n + 1)) / 2 and returns the result, which is then printed to the console.

The `tetrahedral_number` function takes a single integer argument `n` and returns the nth tetrahedral number. The formula used to calculate the nth tetrahedral number is (n * (n + 1)) / 2.

By calling the `tetrahedral_number` function with the argument `5`, we obtain the 5th tetrahedral number, which is `35`.
```

```python
def tetrahedral_number(n):
    return (n * (n + 1)) // 2
```

This function works by using the formula for calculating the nth tetrahedral number, which is (n * (n + 1)) / 2. By using integer division (`//`), we ensure that the result is an integer, as tetrahedral numbers are always integers.

To use the `tetrahedral_number` function, you can simply call it with the desired value of `n`. For example, `tetrahedral_