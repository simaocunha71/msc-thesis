```python
def filterIntegers(values):
    return [value for value in values if isinstance(value, int)]
```
Explanation:

The problem is asking to create a function that filters a given list of values and returns a new list containing only the integers from the original list.

In Python, we can use a list comprehension to achieve this. The `isinstance` function is used to check if a value is an instance of the `int` class. The comprehension iterates over the original list, checks each value with `isinstance`, and includes it in the new list if it's an integer.

For example, if we call `filterIntegers([1, 2, 3, 'abc', {}, []])`, the function will return `[1, 2, 3]` because these are the only integers in the original list. If we call `filterIntegers(['a', 3.14, 5])`, the function will return `[5]` because this is the only integer in the original list.

Note that this implementation assumes that the input list only contains values that are instances of `int`, `float`, `str`, `list`, `dict`, or other built-in Python types. If the input list can contain other types of values, additional checks may be needed.