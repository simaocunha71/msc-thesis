```
def extract_even(nested_tuple):
    result = []
    for item in nested_tuple:
        if isinstance(item, tuple):
            result.append(extract_even(item))
        elif item % 2 == 0:
            result.append(item)
    return tuple(result)
```


The function `extract_even` takes a nested mixed tuple as input and returns a new tuple with only the even elements. It uses recursion to handle nested tuples. For each item in the input tuple, it checks if the item is a tuple itself. If it is, the function calls itself with that tuple as input. If the item is not a tuple, it checks if the item is even. If it is, the function adds it to the result list. Finally, the function returns the result as a tuple. The unit test `assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)` ensures that the function works correctly. 
```python
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
``` 














# 