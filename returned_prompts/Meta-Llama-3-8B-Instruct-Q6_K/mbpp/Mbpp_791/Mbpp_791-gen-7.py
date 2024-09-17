The problem is asking to remove tuples from a given tuple. However, the problem description is not clear about what "remove tuples" means. 

Thanks to the unit test `assert remove_nested((1, 5, 7, (4, 6), 10)) == (1, 5, 7, 10)`, we can understand that the function should remove all tuples from the given tuple. 

Here is the Python solution:

```
def remove_nested(t):
    return tuple(x for x in t if not isinstance(x, tuple))
```

This function uses a generator expression to iterate over the elements in the tuple. It checks if each element is a tuple using the `isinstance` function. If it's not a tuple, it includes it in the resulting tuple. If it is a tuple, it skips it. The resulting tuple is then returned. 