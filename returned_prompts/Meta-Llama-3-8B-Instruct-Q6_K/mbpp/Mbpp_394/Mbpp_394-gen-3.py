```
def check_distinct(t):
    return len(t) == len(set(t))
```
This function takes a tuple `t` as input and returns a boolean value indicating whether the tuple contains no duplicates or not. It does this by comparing the length of the tuple to the length of a set created from the tuple. If the lengths are equal, it means that the tuple contains no duplicates, and the function returns `True`. If the lengths are not equal, it means that the tuple contains duplicates, and the function returns `False`. The unit test `assert check_distinct((1, 4, 5, 6, 1, 4)) == False` ensures that the function returns the correct result for a tuple that contains duplicates.