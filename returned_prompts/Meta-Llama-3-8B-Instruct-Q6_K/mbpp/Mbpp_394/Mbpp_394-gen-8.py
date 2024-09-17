```
def check_distinct(t):
    return len(t) == len(set(t))
```
This function checks if the length of the tuple is equal to the length of a set created from the tuple. In Python, a set is an unordered collection of unique elements. So, if the tuple contains any duplicate elements, the set will have fewer elements than the tuple, and the function will return `False`. Otherwise, it will return `True`.

The unit test `assert check_distinct((1, 4, 5, 6, 1, 4)) == False` shows that the function should return `False` for tuples that contain duplicates. This is because the set `(1, 4, 5, 6, 1, 4)` has 5 elements, which is fewer than the 6 elements in the tuple. Therefore, the function correctly identifies the tuple as containing duplicates.