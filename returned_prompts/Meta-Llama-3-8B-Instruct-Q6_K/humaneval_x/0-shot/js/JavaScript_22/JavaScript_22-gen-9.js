```python
def filterIntegers(values):
    return [value for value in values if isinstance(value, int)]

print(filterIntegers(['a', 3.14, 5]))  # [5]
print(filterIntegers([1, 2, 3, 'abc', {}, []]))  # [1, 2, 3]
``` 