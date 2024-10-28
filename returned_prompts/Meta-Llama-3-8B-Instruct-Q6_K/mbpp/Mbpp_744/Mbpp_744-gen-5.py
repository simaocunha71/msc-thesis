```
def check_none(tup):
    return None in tup
```
The function `check_none` takes a tuple as an argument and returns `True` if the tuple contains `None` and `False` otherwise. This is achieved using the `in` operator which checks if a value is present in a sequence. In this case, it checks if `None` is present in the tuple. 

The unit test `assert check_none((10, 4, 5, 6, None)) == True` ensures that the function returns `True` when the tuple contains `None`. 