def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

assert dict_depth({'a':1,  'b': {'c': {'d': {}}}})==4
"""
Explanation:
The depth of a dictionary is the maximum depth of any of its nested dictionaries. In the case of the provided dictionary, the maximum depth of any of its nested dictionaries is 4.

This is because the dictionary is nested as follows:

{'a':1, 'b': {'c': {'d': {}}}}

Here, the outermost dictionary is at depth 1, 'b' is at depth 2, 'c' is at depth 3, and 'd' is at depth 4. So, the depth of the dictionary is 4.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 2:
<jupyter_code>
