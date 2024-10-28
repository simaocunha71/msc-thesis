```
def check_type(t):
    return len(set(type(i) for i in t)) == 1
```


The function `check_type(t)` takes a tuple `t` as an argument. It uses a generator expression to get the types of all elements in the tuple, converts them to a set (which removes duplicates), and checks if the set has only one element. If it does, that means all elements have the same type, and the function returns `True`. If the set has more than one element, that means there are elements with different types, and the function returns `False`. 

For example, `check_type((5, 6, 7, 3, 5, 6))` returns `True` because all elements are integers. 

This solution passes the given unit test. 







