You can use a set to solve this problem. A set in Python is an unordered collection of unique elements. If the length of the set is equal to the length of the tuple, then the tuple contains no duplicates.

Here is the Python function that solves the problem:

```Python
def check_distinct(t):
    return len(set(t)) == len(t)
```

This function works by converting the tuple to a set, which removes any duplicates. It then compares the length of the set to the length of the original tuple. If they are equal, then the tuple contained no duplicates, and the function returns True. Otherwise, it returns False.

The unit test `assert check_distinct((1, 4, 5, 6, 1, 4)) == False` ensures that the function works correctly when the tuple contains duplicates. In this case, the function should return False because the tuple contains duplicates. If the function returns True in this case, it means that there is a bug in the function. 





```Python
def check_distinct(t):
    return len(set(t)) == len(t)
```





Python function to check if given tuple contains no duplicates. This function works by converting the tuple to a set, which removes any duplicates. It then compares the length of the set to the length of the original tuple. If they are equal, then the tuple contained no duplicates, and the function returns True. Otherwise, it returns False.

The unit test `assert check_distinct((1, 4, 5, 6, 1, 4)) == False` ensures that the function works correctly when the tuple contains duplicates. In this case, the function should return False because the tuple contains duplicates. If the function returns True in this case, it means that there is a bug in the function.