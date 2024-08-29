def drop_empty(dictionary):
    return {key: value for key, value in dictionary.items() if value is not None}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))

"""
Output:
{'c1': 'Red', 'c2': 'Green'}
"""

This function works by using a dictionary comprehension to create a new dictionary that includes only the key-value pairs from the original dictionary where the value is not None. It does this by iterating over the key-value pairs in the original dictionary using the items() method and then excluding any pairs where the value is None.
"""

# 