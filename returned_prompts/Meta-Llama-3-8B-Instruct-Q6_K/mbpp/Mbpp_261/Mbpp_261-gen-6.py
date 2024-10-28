```
def division_elements(t1, t2):
    return tuple(a/b for a, b in zip(t1, t2))
```


This function uses the built-in Python function zip() to pair up corresponding elements from the two input tuples. It then uses a generator expression to perform element-wise division on these pairs, and finally returns the result as a tuple. The unit test provided ensures that the function works correctly for the given input.