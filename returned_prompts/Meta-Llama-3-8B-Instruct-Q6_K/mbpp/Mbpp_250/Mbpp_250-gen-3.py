```
def count_X(tup, element):
    return tup.count(element)
```
This function uses the built-in `count` method of Python's list (and tuple) data type. This method returns the number of occurrences of the element in the tuple. 

For example, if you call `count_X((10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2), 4)`, it will return 0 because the element 4 is not present in the tuple. 