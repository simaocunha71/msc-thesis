```python
import sys

def tuple_size(tup):
    return sys.getsizeof(tup)

assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
```

Explanation:
In this problem, we are asked to write a function that returns the size in bytes of a given tuple. The function `sys.getsizeof()` is a built-in Python function that returns the size of an object in bytes. We are using it to get the size of the tuple. The assertion checks if the function works as expected.


