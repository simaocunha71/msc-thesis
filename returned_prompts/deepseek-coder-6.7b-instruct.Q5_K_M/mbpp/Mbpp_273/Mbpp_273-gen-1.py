Here is the Python code to solve the problem:

```python
def substract_elements(t1, t2):
    if len(t1) != len(t2):
        return 'Tuples must be of the same length'

    return tuple(x1 - x2 for (x1, x2) in zip(t1, t2))

print(substract_elements((10, 4, 5), (2, 5, 18)))
```

This Python code defines a function `substract_elements` that takes in two tuples. It checks if the two tuples have the same length. If they do not, it returns an error message. If they do, it computes the subtraction of the elements at the same index in the two tuples and returns the result as a new tuple. The `zip` function is used to pair the elements at the same index in the two tuples. The