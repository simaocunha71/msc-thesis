```
def all_unique(lst):
    return len(lst) == len(set(lst))
```


Here is the explanation of the code:

*   The function `all_unique` takes a list `lst` as an argument.
*   It compares the length of the list `lst` with the length of a set created from the list.
*   In Python, a set is an unordered collection of unique elements. So, if the length of the set is equal to the length of the list, it means that all elements in the list are unique.
*   If the lengths are equal, the function returns `True`; otherwise, it returns `False`. This indicates whether all elements in the list are unique or not.

The unit test `assert all_unique([1,2,3]) == True` ensures that the function correctly identifies a list with unique elements. If the function is implemented correctly, this test will pass.