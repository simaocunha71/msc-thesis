def dict_depth(d):
    return max(map(dict_depth, d.values())) + 1 if isinstance(d, dict) else 0


"""
The above code uses recursion to find the depth of a dictionary. It returns the maximum depth of all the values in a dictionary, plus one for the current depth. It checks if the object is a dictionary using the isinstance function, and if not, returns 0.
"""


# Test
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4


"""
The test case checks if the function returns the correct depth for a dictionary with nested dictionaries. In this case, the depth is 4, which is the maximum depth of the nested dictionaries.
"""


# Other Test Cases

assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert