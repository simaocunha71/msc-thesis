```
def extract_even(t):
    return tuple(x if isinstance(x, tuple) else (x,) if x % 2 == 0 else () for x in t)
```


The problem is asking to write a function that takes a nested mixed tuple (a tuple containing both integers and other tuples) as an input. The function should return a new tuple containing only the even elements. The even elements are integers that are divisible by 2, and tuples that contain only even elements.

For example, the unit test `assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)` shows that the function should return a new tuple containing only the even elements.

Here is a Python solution for the problem:

```
def extract_even(t):
    return tuple(x if isinstance(x, tuple) else (x,) if x % 2 == 0 else () for x in t)
```

This function uses a generator expression to iterate over the input tuple. If an element is a tuple, it recursively calls the function on that tuple. If an element is an integer, it checks if the integer is even and returns a tuple containing the integer if it is, or an empty tuple if it is not. The result is a new tuple containing only the even elements. 