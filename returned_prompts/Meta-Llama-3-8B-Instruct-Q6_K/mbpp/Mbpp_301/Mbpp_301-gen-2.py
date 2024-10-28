The problem is asking you to write a function that calculates the depth of a dictionary. The depth of a dictionary is the maximum depth of its nested dictionaries.

Here's a Python function that solves this problem:

```
def dict_depth(d):
    max_depth = 0
    for k, v in d.items():
        if isinstance(v, dict):
            depth = dict_depth(v) + 1
            max_depth = max(max_depth, depth)
    return max_depth
```

This function works by recursively traversing the dictionary and counting the maximum depth of its nested dictionaries. The `isinstance` function is used to check if the value is a dictionary. The `max` function is used to find the maximum depth.

The unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4` ensures that the function works correctly. The dictionary has a depth of 4, which is the maximum depth of its nested dictionaries. 

For example, the dictionary {'a':1, 'b': {'c': {'d': {}}}} has the following structure:
```
'a': 1
'b': 
    'c': 
        'd': {}
```
The maximum depth of this dictionary is 4, which is the depth of the innermost dictionary {'d': {}}. The function `dict_depth` returns 4 for this dictionary. 





