The problem is to create a function that calculates the depth of a dictionary. The depth of a dictionary is the number of levels it has, where each level is a dictionary. The function should return the maximum depth.

The unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4` suggests that the function should return the maximum depth of the dictionary. For example, the dictionary `{'a':1, 'b': {'c': {'d': {}}}}` has a depth of 4.

Here is the Python solution:
```
def dict_depth(d, depth=1):
    if not isinstance(d, dict):
        return depth
    max_depth = depth
    for key, value in d.items():
        max_depth = max(max_depth, dict_depth(value, depth + 1))
    return max_depth
```


This function works by recursively going through each item in the dictionary. If the item is not a dictionary, it returns the current depth. If the item is a dictionary, it calls itself with the new dictionary and the current depth plus one. The maximum depth found is returned at the end. The initial depth is set to 1, and the function returns the maximum depth found. The function also checks if the item is a dictionary using the `isinstance` function. If the item is not a dictionary, it returns the current depth. This ensures that the function does not go into an infinite loop if the dictionary contains non-dictionary values.