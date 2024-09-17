```
def check_Consecutive(lst):
    return all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))
```
This function uses the built-in `all` function in Python, which returns `True` if all elements of the iterable (in this case, a generator expression) are true. The generator expression `lst[i] + 1 == lst[i+1] for i in range(len(lst)-1)` checks if each element in the list is one more than the previous one. If this condition is met for all elements, the function returns `True`, indicating that the list contains consecutive numbers. Otherwise, it returns `False`. The unit test `assert check_Consecutive([1,2,3,4,5]) == True` confirms this behavior. 

For example, if you call `check_Consecutive([1,2,3,4,5])`, the function will return `True` because the list contains consecutive numbers. If you call `check_Consecutive([1,2,4,5])`, the function will return `False` because the list does not contain consecutive numbers. 