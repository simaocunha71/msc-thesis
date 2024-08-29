Here is a Python solution using recursion:

```python
def dict_depth(d):
    if not isinstance(d, dict) or not d:  # if dictionary is empty or not a dictionary
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
```

Here, we use recursion to keep going deeper into the dictionary until we hit the base case of an empty or non-dictionary value. We then count up the layers of depth.

Note that this function returns 1 for an empty dictionary, as it is technically a depth of 1 (it has 1 layer, even if it's empty). If you want the depth to be 0 for an empty dictionary, you can modify the base case to return 0.
"""

