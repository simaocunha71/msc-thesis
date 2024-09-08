Here is the Python code to solve the problem:

```python
def dict_filter(d, n):
    return {key: value for key, value in d.items() if value >= n}

d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
n = 170
print(dict_filter(d, n))
```

This code uses dictionary comprehension to create a new dictionary that includes only those entries where the value is greater than or equal to n. The `items()` method is used to iterate over the key-value pairs in the dictionary, and the `if` condition filters out those pairs where the value is less than n.
"""

