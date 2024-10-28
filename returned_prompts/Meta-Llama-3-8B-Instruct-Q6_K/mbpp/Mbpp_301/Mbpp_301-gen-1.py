```
def dict_depth(d):
    depth = 1
    for k, v in d.items():
        if isinstance(v, dict):
            depth = max(depth, 1 + dict_depth(v))
    return depth
```


The function `dict_depth(d)` calculates the depth of the dictionary `d`. It does this by iterating over each key-value pair in the dictionary. If the value is itself a dictionary, the function calls itself recursively with that dictionary, and takes the maximum of the current depth and the depth of the recursive call. The function returns the final depth. The unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4` shows that the function correctly calculates the depth of a dictionary with multiple levels of nesting. 





In this problem, we are asked to write a function that calculates the depth of a dictionary. The depth of a dictionary is the maximum number of levels of nesting in the dictionary. For example, the dictionary `{'a':1, 'b': {'c': {'d': {}}}}` has a depth of 4.

The problem is solved by defining a recursive function `dict_depth(d)` that calculates the depth of a dictionary `d`. The function iterates over each key-value pair in the dictionary. If the value is itself a dictionary, the function calls itself recursively with that dictionary, and takes the maximum of the current depth and the depth of the recursive call. The function returns the final depth.

The unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4` shows that the function correctly calculates the depth of a dictionary with multiple levels of nesting. The test passes because the function returns 4, which is the correct depth of the dictionary.

Here is the solution in Python:
```
def dict_depth(d):
    depth = 1
    for k, v in d.items():
        if isinstance(v, dict):
            depth = max(depth, 1 + dict_depth(v))
    return depth
```
This function works by iterating over each key-value pair in the dictionary. If the value is itself a dictionary, the function calls itself recursively with that dictionary, and takes the maximum of the current depth and the depth of the recursive call. The function returns the final depth.