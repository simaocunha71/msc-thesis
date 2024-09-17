```
def check_distinct(t):
    return len(t) == len(set(t))
```


The unit test `assert check_distinct((1, 4, 5, 6, 1, 4)) == False` suggests that the function should return `False` if the tuple contains duplicates. 

The function `check_distinct` uses the fact that a set in Python is an unordered collection of unique elements. If the length of the tuple is equal to the length of the set created from the tuple, then the tuple does not contain any duplicates. Otherwise, it does contain duplicates.

Here, `len(t)` gives the number of elements in the tuple, and `len(set(t))` gives the number of unique elements in the tuple. If these two lengths are equal, then the tuple contains no duplicates, so the function returns `True`. Otherwise, it returns `False`. 

For example, `check_distinct((1, 4, 5, 6, 1, 4))` will return `False` because the tuple contains the duplicate elements 1 and 4. On the other hand, `check_distinct((1, 4, 5, 6))` will return `True` because the tuple does not contain any duplicates. 