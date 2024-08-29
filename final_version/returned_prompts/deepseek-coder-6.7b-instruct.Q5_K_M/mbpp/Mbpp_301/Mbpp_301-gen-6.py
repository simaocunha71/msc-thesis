Here is the Python function for the problem:

```python
def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))  # Outputs: 4
```

In this function, we first check if the given object is a dictionary and not empty. If it's not, we return 1, which is the base level of the dictionary.
Then we recursively call dict_depth for all the values in the dictionary. The result is the maximum of these calls plus 1, which gives us the depth of the dictionary.

This function works by exploring each branch of the dictionary and counting the number of layers it goes down. It uses recursion, a key feature in Python, to traverse all levels of the dictionary.
"""

def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))  # Outputs: 4
```
"""

