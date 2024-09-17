```
def find_substring(lst, sub):
    return any(sub in s for s in lst)
```
This function uses the built-in `any` function, which returns `True` if at least one element of the iterable (in this case, a generator expression) is true. The generator expression `sub in s for s in lst` checks if the substring `sub` is present in each string `s` in the list `lst`. If any of these checks return `True`, the `any` function returns `True`. If none of the checks return `True`, the `any` function returns `False`. 

The unit test `assert find_substring(["red", "black", "white", "green", "orange"],"ack")==True` shows that the function should return `True` if the substring is found in any of the strings in the list. 

The function will return `False` if the substring is not found in any of the strings in the list. For example, `find_substring(["red", "black", "white", "green", "orange"],"blue")` would return `False`. 