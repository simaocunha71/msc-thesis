Here is a Python solution for the problem:

```python
def filterIntegers(values):
    return [v for v in values if isinstance(v, int)]

print(filterIntegers(['a', 3.14, 5]))  # Output: [5]
print(filterIntegers([1, 2, 3, 'abc', {}, []]))  # Output: [1, 2, 3]
```

Explanation:

The `filterIntegers` function takes a list `values` as input. It uses a list comprehension to iterate over the values and checks if each value is an instance of `int` using the `isinstance` function. If the value is an integer, it is included in the output list. The function returns the filtered list of integers.

The `print` statements demonstrate the usage of the `filterIntegers` function with different inputs, which produce the expected outputs.