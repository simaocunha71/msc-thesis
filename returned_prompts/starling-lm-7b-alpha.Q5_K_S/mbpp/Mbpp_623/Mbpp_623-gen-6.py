"""
Here is a simple solution using Python's built-in map function:

def nth_nums(nums, n):
    return list(map(lambda x: x**n, nums))
"""

Here is a simple solution using Python's built-in map function:

```python
def nth_nums(nums, n):
    return list(map(lambda x: x**n, nums))
```

This solution first uses the `map` function to apply the `lambda` function to each element in the `nums` list. The `lambda` function takes an element `x` and returns the number raised to the power `n`. The `map` function then returns an iterable, which is converted into a list using the `list` function.

For example, if we call `nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)`, the function will return `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`.

The `lambda` function is an anonymous function that takes one or more arguments and returns an expression. In this case, the expression is `x**n`, which calculates `x` raised to the power `n`.

The `map` function applies the provided function to each item of an iterable (like a list) and returns a list of the results. In this case, it applies the `lambda` function to each element in the `nums` list.

Finally, the `list` function is used to convert the iterable returned by the `map` function into a list, which is then returned by the `nth_nums` function.

This solution uses Python's built-in functions to perform the operation in a concise and efficient manner.

```python
def nth_nums(nums, n):
    return list(map(lambda x: x**n, nums))
```

This code defines a function `nth_nums` that takes two arguments: `nums`, a list of numbers, and `n`, the exponent