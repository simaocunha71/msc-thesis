```
def check_type(t):
    return len(set(type(i) for i in t)) == 1
```
The function `check_type` takes a tuple `t` as an argument. It uses a generator expression to create a set of types of elements in the tuple. If the length of this set is 1, it means all elements have the same type, so the function returns `True`. If the length is more than 1, it means there are elements with different types, so the function returns `False`. This function passes the given unit test. 

The unit test `assert check_type((5, 6, 7, 3, 5, 6) ) == True` checks if the function returns `True` for a tuple of integers. 

For example, if you call `check_type((5, 6, 7, 3, 5, 6))`, the function will return `True` because all elements in the tuple are integers. If you call `check_type((5, '6', 7, 3, 5, '6'))`, the function will return `False` because there are elements with different types (integer and string). 