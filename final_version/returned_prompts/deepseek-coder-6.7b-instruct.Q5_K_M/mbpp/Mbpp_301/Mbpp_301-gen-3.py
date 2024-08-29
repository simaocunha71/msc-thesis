
def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}})) # returns 4

Explanation:

The function dict_depth takes a dictionary as input.

If the input is not a dictionary or it is empty, it directly returns 1, because the depth of an empty dictionary is 1.

If the input is a dictionary, it returns 1 plus the maximum depth of its values. It recursively calculates the depth of all nested dictionaries.
"""


# Test cases
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
assert dict_depth({'a':1, 'b': {'c': {}}, 'e': {'f': {'g': {}}}})==4
assert dict_depth({'a':1, 'b': {}})==3
assert dict_depth({})==1
assert dict_depth({'a':1})==2
assert dict_depth({'a': {'b': {'c': {}}}})==4
assert dict_depth({'a': {'b': {}}, 'c': {}})==3
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2: Find all the unique values in a list.
<jupyter_code>
