Here is the Python code to solve the problem:

```python
def all_prefixes(string: str) -> List[str]:
    return [string[0:i+1] for i in range(len(string))]
```

This function uses list comprehension to create a list of all prefixes from the input string. It iterates over the range of indices of the string and for each index, it slices the string from the start to the index plus one. This results in a list of all prefixes of the string.

Let's test this function with the provided example:

```python
print(all_prefixes('abc'))  # Output: ['a', 'ab', 'abc']
```

This output matches the expected result.
"""

