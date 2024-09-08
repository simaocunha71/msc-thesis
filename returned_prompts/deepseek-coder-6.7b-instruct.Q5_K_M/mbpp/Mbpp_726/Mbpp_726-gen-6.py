Here is the Python function for the problem:

```python
def multiply_elements(t):
    return tuple(t[i] * t[i+1] for i in range(len(t)-1))
```

You can test the function with the provided example:

```python
print(multiply_elements((1, 5, 7, 8, 10)))  # Output: (5, 35, 56, 80)
```

The function `multiply_elements` works by using a generator expression to generate the elements of the output tuple. For each index `i` in the range from 0 to `len(t) - 1` (exclusive), the expression `t[i] * t[i+1]` computes the i-th element of the output tuple. The generator expression is then passed to the `tuple()` function to create the output tuple.
"""

