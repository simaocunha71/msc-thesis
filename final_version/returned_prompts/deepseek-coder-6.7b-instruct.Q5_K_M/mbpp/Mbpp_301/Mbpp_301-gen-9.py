
def dict_depth(d):
    if not isinstance(d, dict):
        return 0
    if not d:
        return 1
    depths = [dict_depth(v) for v in d.values()]
    return max(depths) + 1

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))

"""
The function works by recursively calling itself on each value in the dictionary.
If the value is not a dictionary, it returns 0, as there's no "depth" in a non-dictionary value.
If the dictionary is empty, it returns 1, because we are at least one level deep.
The maximum depth of the dictionary is the maximum depth of its values plus 1 for the current level.
"""
<jupyter_output>
4
<jupyter_text>
Problem 3
<jupyter_code>
