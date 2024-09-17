```
def get_equal(tuples):
    return len(set(map(len, tuples))) == 1
```


This function works by first mapping the `len` function to each tuple in the input list, which gives a list of lengths. It then converts this list to a set, which removes any duplicates. If all the tuples had the same length, the set will contain only one element, which is the length. Therefore, the function returns whether the length of the set is 1 or not.

For example, if you call `get_equal([(11, 22, 33), (44, 55, 66)])`, the function will return `True` because all the tuples have the same length. If you call `get_equal([(11, 22), (44, 55, 66)])`, the function will return `False` because the tuples do not all have the same length.