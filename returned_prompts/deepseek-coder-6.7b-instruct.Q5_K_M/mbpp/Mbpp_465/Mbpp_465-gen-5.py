def drop_empty(dic):
    return {k: v for k, v in dic.items() if v}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))

"""
In the function 'drop_empty' we use dictionary comprehension to create a new dictionary. For each key-value pair in the original dictionary, if the value is not None or False, it's included in the new dictionary. This effectively removes any pairs where the value is None or False.
"""

