```
def _sum(input_list):
    """
    Find the sum of an array
    >>> _sum([1, 2, 3])
    6
    """
    return sum(input_list)
```

In this example, the function `_sum` is defined to take an input list and return the sum of all elements in the list. The `sum` function is a built-in Python function that adds up all the elements in an iterable (like a list) and returns the total. By passing the `input_list` as an argument to the `sum` function, we can calculate the sum of all the elements in the input list and return it as the result of the function.

To test the function, we use the `assert` statement to verify that the function returns the expected result when given the example input `[1, 2, 3]`. If the assertion passes, it means that the function is correctly calculating the sum of the array.

You can call this function with any array of numbers to calculate the sum. For example, `_sum([4, 5, 6])` would return `15`, and `_sum([-1, 2, 3])` would return `4`.

Note: The `assert` statement is used here for testing purposes only and is not necessary for the function to work correctly. It is a way to check if the function is behaving as expected during development and debugging.

```python
def _sum(input_list):
    """
    Find the sum of an array
    >>> _sum([1, 2, 3])
    6
    """
    return sum(input_list)
```

This code defines a function `_sum` that takes an input list as a parameter. The `sum` function is then called with the `input_list` as an argument, and the result is returned as the output of the `_sum` function.

The `assert` statement is used to check if the function returns the expected result when given the example input `[1, 2, 3]`. If the assertion passes, it means that the function is correctly calculating the sum of the array.

You can use this function to find the sum of any array of numbers by calling it with the desired