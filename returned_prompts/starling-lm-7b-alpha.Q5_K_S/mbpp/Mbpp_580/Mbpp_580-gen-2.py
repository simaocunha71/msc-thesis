Here is a function that removes uneven elements in the nested mixed tuple:

```python
def extract_even(t):
    """
    >>> extract_even((4, 5, (7, 6, (2, 4)), 6, 8))
    (4, (6, (2, 4)), 6, 8)
    """
    if isinstance(t, tuple):
        new_t = []
        for elem in t:
            if isinstance(elem, tuple):
                new_t.append(extract_even(elem))
            elif isinstance(elem, int):
                if elem % 2 == 0:
                    new_t.append(elem)
        return tuple(new_t)
    else:
        return t
```

This function checks if the input `t` is a tuple. If it is, it initializes an empty list `new_t`. Then, it iterates over each element in `t`. If an element is also a tuple, the function calls itself recursively with that element. If an element is an integer, the function checks if it is even (i.e., its remainder when divided by 2 is 0). If it is even, the function appends it to `new_t`. Finally, the function returns a tuple of the elements in