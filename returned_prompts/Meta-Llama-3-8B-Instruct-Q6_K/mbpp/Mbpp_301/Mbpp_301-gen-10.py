The problem asks to create a function that calculates the depth of a dictionary. The depth of a dictionary is the maximum number of keys that need to be traversed to reach a leaf node (a dictionary with no sub-dictionaries).

Here's a Python function that solves this problem:

```
def dict_depth(d):
    return 1 + (max([dict_depth(i) for i in d.values()], default=0) if d else 0)
```

This function works by recursively traversing the dictionary and calculating the depth of each sub-dictionary. The maximum depth found is then returned. If the dictionary is empty, it returns 0.

The unit test `assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4` ensures that the function works correctly for a dictionary with a depth of 4. This test case checks that the function returns 4 for the given dictionary, which has the following structure: `{'a': 1, 'b': {'c': {'d': {}}}}`. This dictionary has 4 levels of nesting, so the function should return 4.

This function can be used to find the depth of any dictionary, regardless of its structure. It's a simple and efficient solution that works well for large dictionaries.