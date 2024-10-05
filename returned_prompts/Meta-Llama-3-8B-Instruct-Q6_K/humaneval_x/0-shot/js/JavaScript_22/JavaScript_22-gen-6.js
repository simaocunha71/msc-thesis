Here is a Python function that filters a list of values and returns a new list containing only the integers:

```python
def filterIntegers(values):
    return [value for value in values if isinstance(value, int)]
```

This function uses a list comprehension to iterate over the input list `values`. For each value, it checks if the value is an integer using the `isinstance` function. If the value is an integer, it is included in the output list. If not, it is skipped.

Here's an example usage of this function:

```python
print(filterIntegers(['a', 3.14, 5]))  # Output: [5]
print(filterIntegers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

I hope this helps! Let me know if you have any further questions.