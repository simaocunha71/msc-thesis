def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

# Test
print(dict_depth({'a':1,  'b': {'c': {'d': {}}}})) # Expected output: 4

# Note: This function works by recursively checking the depth of each nested dictionary.
# The base case is an empty dictionary or a non-dictionary value, where the depth is 1.
# The recursive case is a dictionary with nested dictionaries, where the depth is 1 plus the maximum depth of the nested dictionaries.
<jupyter_output>
4
<jupyter_text>
Question 3: Write a Python function to perform a binary search.
<jupyter_code>
