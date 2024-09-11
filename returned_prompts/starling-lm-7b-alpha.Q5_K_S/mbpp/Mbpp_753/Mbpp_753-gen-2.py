"""
def min_k(tuples, k):
    tuples.sort(key=lambda x: x[1])
    return tuples[:k]

assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
"""

Here is a function to find minimum k records from tuple list:

```python
def min_k(tuples, k):
    tuples.sort(key=lambda x: x[1])
    return tuples[:k]
```

In this function, we first sort the tuples based on the second element (the score) using the `sort()` method with a lambda function as the key. This ensures that the tuples are sorted in ascending order based on the score. Then, we return a slice of the first `k` elements from the sorted list using the `[:k]` notation.

To verify the function, we can use the `assert` statement to check if the result of the function matches the expected output. In this case, we assert that `min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2)` returns `[('Akash', 2), ('Akshat', 4)]`, which is the expected output.

By running this code, the assertion will pass if the function correctly finds the minimum `k` records from the tuple list.
```

```python
def min_k(tuples, k):
    tuples.sort(key=lambda x: x[1])
    return tuples[:k]

assert min_k([('Manjeet', 10), ('Akshat', 4), ('Akash', 2), ('Nikhil', 8)], 2) == [('Akash', 2), ('Akshat', 4)]
```

This code will return `True` if the function correctly finds the minimum `k` records from the tuple list, and `False`