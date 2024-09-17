You can solve this problem by using a list comprehension in Python. The list comprehension will iterate over the indices and values of the tuples, subtract the corresponding values of the second tuple from the first tuple, and then convert the list back to a tuple.

Here is the Python function that does this:
```
def substract_elements(t1, t2):
    return tuple(t1[i] - t2[i] for i in range(len(t1)))
```
This function works by using a generator expression to iterate over the indices and values of the tuples. The expression `t1[i] - t2[i]` subtracts the corresponding values of the second tuple from the first tuple. The `tuple()` function is then used to convert the list back to a tuple.

The unit test `assert substract_elements((10, 4, 5), (2, 5, 18)) == (8, -1, -13)` passes, which confirms that the function works correctly. 