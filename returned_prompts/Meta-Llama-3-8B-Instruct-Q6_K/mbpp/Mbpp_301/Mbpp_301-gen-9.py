The problem is asking to create a function that calculates the depth of a dictionary. The depth of a dictionary is the number of nested dictionaries it contains.

The unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4` helps to understand the problem better. It shows that the function should return the depth of the dictionary, which is 4 in this case.

Here is a Python function that solves the problem:
```
def dict_depth(d, depth=1):
    max_depth = depth
    for k, v in d.items():
        if isinstance(v, dict):
            max_depth = max(max_depth, dict_depth(v, depth+1))
    return max_depth
```
This function works by recursively traversing the dictionary. It starts with a depth of 1 and increments the depth for each nested dictionary it encounters. The maximum depth encountered is returned as the result. If the dictionary is not nested (i.e., it only contains non-dictionary values), the function returns the current depth. 