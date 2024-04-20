"""
Write a function to find the depth of a dictionary.
assert dict_depth({'a':1, 'b': {'c': {'d': {}}}})==4
"""

def find_depth(dict):
    """
    time complexity = O(N)
    space complexity=O(N)
        """
    depth = 0
    for key in dict.keys():
        if isinstance(key, list):
            depth+=1
            return depth
        else:
            try:
                depth += find_depth(dict[key])
            except KeyError:
                depth += 1
    print(find_depth)
