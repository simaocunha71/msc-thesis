"""
def get_equal(tuples):
    for i in range(len(tuples)):
        if len(tuples[i]) != len(tuples[0]):
            return False
    return True

# Testing
print(get_equal([(11, 22, 33), (44, 55, 66)]))
"""

In Python, you can use the `zip` function to iterate over two lists simultaneously. In this case, you can use it to check if the length of each tuple in the list is equal to the length of the first tuple. Here's an example implementation:

```python
def get_equal(tuples):
    return all(map(len, tuples) == len(tuples[0]))
```

This `get_equal` function will return `True` if all tuples in the `tuples` list have the same length as the first tuple. Otherwise, it will return `False`. The `map` function is used to apply the `len` function to each tuple in the `tuples` list, and the `all` function is used to check if all results are equal to the length of the first tuple.

To test the function, you can use the `print` statement to print the result of the function call with a sample list of tuples:

```python
print(get_equal([(11, 22, 33), (44, 55, 66)]))
```

This will output `True` if all tuples in the list have the same length as the first tuple, and `False` otherwise.

Note: The `all` function returns `False` as soon as it encounters a `False` value, so if any tuple in the list has a different length than the first tuple, the function will immediately return `False`.
```

```

```python
def get_equal(tuples):
    for i in range(len(tuples)):
        if len(tuples[i]) != len(tuples[0]):
            return False
    return True

# Testing
print(get_equal([(11, 22, 33), (44, 5