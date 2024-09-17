```
def check_type(tup):
    return len(set(type(x) for x in tup)) == 1
```
The function `check_type` takes a tuple as an argument and returns a boolean value indicating whether all elements in the tuple have the same data type or not.

The `set(type(x) for x in tup)` expression creates a set of the types of all elements in the tuple. The `len` function is used to get the number of unique types in the set. If there is only one unique type, then all elements have the same data type, and the function returns `True`. Otherwise, it returns `False`.

The provided unit test `assert check_type((5, 6, 7, 3, 5, 6) ) == True` suggests that the function should return `True` for a tuple containing integers. Therefore, the function is implemented to check if all elements in the tuple have the same data type. If they do, the function returns `True`; otherwise, it returns `False`. 