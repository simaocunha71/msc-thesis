```
def count_X(tup, elem):
    return tup.count(elem)
```
This function uses the built-in `count` method of Python's tuple data type, which returns the number of occurrences of the specified element in the tuple.

The unit test `assert count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2),4) == 0` ensures that the function works correctly, as it checks that the count of the element 4 in the tuple is 0, which is the expected result. 