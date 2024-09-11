Here's a function that does what you're asking for:

```python
def tuple_size(*args):
    return sum(sys.getsizeof(arg) for arg in args)
```

And here's a test case for it:

```python
import sys

def test_tuple_size():
    assert tuple_size("A", 1, "B", 2, "C", 3) == sys.getsizeof(("A", 1, "B", 2, "C", 3))

test_tuple_size()
```

This function works by using Python's built-in `sys.getsizeof` function to get the size of each item in the tuple, then summing them up to find the total size of the tuple.

```python
import sys

def tuple_size(*args):
    return sum(sys.getsizeof(arg) for arg in args)
```

The `*args` syntax in the function definition means that you can pass in as many arguments as you like, and they'll all be added up to find the total tuple size.

```python
def test_tuple_size():
    assert tuple_size("A", 1, "B", 2, "C", 3) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
```

The `test_tuple_size` function is a simple test case that checks whether the `tuple_size` function gives the same result as the `sys.getsizeof` function for a specific tuple.

```python
test_tuple_size()
```

Finally, calling `test_tuple_size()` runs the test case and checks that the `tuple_size` function works correctly.

```python
import sys

def tuple_size(*args):
    return sum(sys.getsizeof(arg) for arg in args)
```

```python
def test_tuple_size():
    assert tuple_size("A", 1, "B", 2, "C", 3) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
```