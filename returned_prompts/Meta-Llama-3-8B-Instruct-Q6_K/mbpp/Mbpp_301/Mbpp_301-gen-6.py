```
def dict_depth(d):
    if isinstance(d, dict):
        if not d:
            return 1
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
```
The function `dict_depth` calculates the depth of a dictionary `d`. If `d` is a dictionary, it recursively calls itself on each value in `d` and returns the maximum depth plus one. If `d` is not a dictionary (i.e., it's a leaf node), it returns 0. 

For example, for the dictionary `{'a':1, 'b': {'c': {'d': {}}}}`, the function will return 4, because the maximum depth is 4 (the dictionary has 3 levels of nesting). 

This solution passes the given unit test:
```
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
```  ```python
def dict_depth(d):
    if isinstance(d, dict):
        if not d:
            return 1
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
```
The function `dict_depth` calculates the depth of a dictionary `d`. If `d` is a dictionary, it recursively calls itself on each value in `d` and returns the maximum depth plus one. If `d` is not a dictionary (i.e., it's a leaf node), it returns 0. 

For example, for the dictionary `{'a':1, 'b': {'c': {'d': {}}}}`, the function will return 4, because the maximum depth is 4 (the dictionary has 3 levels of nesting). 

This solution passes the given unit test:
```
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
```  ```python
def dict_depth(d):
    if isinstance(d, dict):
        if not d:
            return 1
        return 1 + max(dict_depth(v) for v in d.values())
    return 0
```
The function `dict_depth` calculates the depth of a dictionary `d`. If `d` is a dictionary, it recursively calls itself on each value in `d` and returns the maximum depth plus one. If `d` is not a dictionary (i.e., it's a leaf node), it returns 0. 

For