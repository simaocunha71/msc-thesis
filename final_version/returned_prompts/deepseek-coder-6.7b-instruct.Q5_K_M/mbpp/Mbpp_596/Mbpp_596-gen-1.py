You can use the sys.getsizeof() function to find the size of an object in bytes. But, there is a catch, sys.getsizeof() does not include the size of the elements of a tuple. 

To get the accurate size of a tuple, you need to recursively add up the sizes of all the elements in the tuple.

Here is a function that does that:

```python
import sys

def get_size_of_tuple_elements(tup):
    size = 0
    for element in tup:
        if isinstance(element, tuple):
            size += get_size_of_tuple_elements(element)
        else:
            size += sys.getsizeof(element)
    return size

def tuple_size(tup):
    return sys.getsizeof(tup) + get_size_of_tuple_elements(tup)
```

This function first gets the size of the tuple object itself (sys.getsizeof(tup)), then it recursively adds the sizes of all elements in the tuple, taking into account nested tuples.

Please note that the size of the elements of the tuple can be different depending on the Python version, the platform, and the compiler.
"""


def test_tuple_size():
    assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))
    assert tuple_size(("A", 1, ("B", 2, "C", 3), 4)) == sys.getsizeof(("A", 1, ("B", 2, "C", 3), 4))
    assert tuple_size(("A", 1, ("B", 2, ("C", 3, 4), 5), 6)) == sys.getsizeof(("A", 1, ("B", 2, ("C", 3, 4), 5), 6))
    assert tuple_size(("A", 1, ("B", 2, ("C", 3, ("D", 4, 5), 6), 7), 8))