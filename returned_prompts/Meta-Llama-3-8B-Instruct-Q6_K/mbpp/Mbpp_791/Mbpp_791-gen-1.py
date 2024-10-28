"""
You can solve this problem by using a generator expression to filter out the non-tuples from the given tuple. Here's how you can do it:

```
def remove_nested(t):
    return tuple(x for x in t if not isinstance(x, tuple))
```

This function works by iterating over each element in the given tuple. If the element is not a tuple, it is included in the new tuple. If the element is a tuple, it is not included. The result is a new tuple with all the non-tuple elements from the original tuple.

For example, if you call `remove_nested((1, 5, 7, (4, 6), 10))`, the function will return `(1, 5, 7, 10)`, which is the desired output. The nested tuple `(4, 6)` has been removed. """


# Test the function
print(remove_nested((1, 5, 7, (4, 6), 10)))  # Output: (1, 5, 7, 10)