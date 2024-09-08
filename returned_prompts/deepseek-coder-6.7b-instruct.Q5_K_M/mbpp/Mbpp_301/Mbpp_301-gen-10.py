
def dict_depth(d):
    if not isinstance(d, dict) or not d:
        return 1
    return 1 + max(dict_depth(v) for v in d.values())

print(dict_depth({'a':1, 'b': {'c': {'d': {}}}}))

"""
Explanation:
The function dict_depth() takes a dictionary as input. If the dictionary is empty or not a dictionary, it returns 1.
If the dictionary is not empty and is a dictionary, it adds 1 to the maximum recursive depth of its values.
"""

# Task 3
