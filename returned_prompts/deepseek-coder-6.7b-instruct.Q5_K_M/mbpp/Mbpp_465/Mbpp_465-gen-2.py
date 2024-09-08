
def drop_empty(d):
    return {k: v for k, v in d.items() if v is not None}

print(drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None}))

"""
This solution uses a dictionary comprehension to create a new dictionary that only includes items from the original dictionary where the value is not None.
"""

# Q2
