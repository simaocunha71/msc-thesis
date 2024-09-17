```
def check_distinct(t):
    return len(set(t)) == len(t)
```


Explanation:
The problem is asking to create a function that checks if a given tuple contains no duplicates. 

The unit test `assert check_distinct((1, 4, 5, 6, 1, 4)) == False` suggests that the function should return `False` when the tuple contains duplicates. 

To solve this problem, we can convert the tuple to a set, which removes any duplicates. We can then compare the lengths of the original tuple and the set. If they are equal, it means that there were no duplicates in the tuple, and we can return `True`. If they are not equal, it means that there were duplicates, and we can return `False`.

Here is the solution in Python:
```
def check_distinct(t):
    return len(set(t)) == len(t)
```
This function works by converting the tuple `t` to a set using the `set` function. The `set` function removes any duplicates from the tuple, so if the tuple contained duplicates, the set will be smaller than the original tuple. The function then compares the lengths of the original tuple and the set using the `len` function. If the lengths are equal, the function returns `True`, indicating that the tuple contained no duplicates. If the lengths are not equal, the function returns `False`, indicating that the tuple contained duplicates.