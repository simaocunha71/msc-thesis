def add_dict_to_tuple(t, d):
    t += (d, )
    return t

t = (4, 5, 6)
d = {"MSAM"  : 1, "is" : 2, "best"  : 3}
print(add_dict_to_tuple(t, d))  # (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})

"""
Here, the function add_dict_to_tuple takes a tuple and a dictionary as input. 
It adds the dictionary to the tuple using the += operator and returns the resulting tuple.
"""

