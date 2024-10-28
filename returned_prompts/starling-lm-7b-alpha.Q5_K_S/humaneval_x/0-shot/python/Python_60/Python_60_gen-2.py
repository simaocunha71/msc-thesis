To solve this problem, you can use the formula for the sum of an arithmetic series, which is given by:

sum = n * (n + 1) / 2

where n is the number up to which you want to sum the numbers.

Here's how you can implement this in Python:

```python
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return n * (n + 1) // 2
```

This function takes an integer `n` as input and returns the sum of all numbers from 1 to `n`. The formula `n * (n + 1) // 2` is used to calculate the sum. The `//` operator is used to perform integer division, which is necessary to ensure the result is an integer. 

You can then use this function to sum up numbers up to a specific value of `n` by calling `sum_to_n(n)` and passing in the desired value of `n`.

For example, if you want to sum up all numbers from 1 to 30, you can call the function like this:

```python
print(sum_to_n(30))  # Output: 465
```

And if you want to sum up all numbers from 1 to 100, you can call the function like this:

```python
print(sum_to_n(100))  # Output: 5050
```

This function will give you the correct sum of all numbers from 1 to `n`.




















































