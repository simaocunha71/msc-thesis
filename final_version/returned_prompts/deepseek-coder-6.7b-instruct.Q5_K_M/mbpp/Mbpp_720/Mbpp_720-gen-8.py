
def add_dict_to_tuple(tup, dic):
    return tup + (dic,)

print(add_dict_to_tuple((4, 5, 6), {"MSAM"  : 1, "is"  : 2, "best"  : 3} ))

# Output: (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})

"""
This function takes a tuple and a dictionary as inputs and returns a new tuple that is a combination of the input tuple and the input dictionary. This is done by concatenating the dictionary to the end of the tuple using the '+' operator, which results in a new tuple.
"""

"""
Note: 
In Python, tuples are immutable. Therefore, you cannot add an element to a tuple once it is created. The '+' operator can be used to concatenate two tuples, but it cannot be used to add an element to an existing tuple. This is why the function returns a new tuple, rather than modifying the original tuple.
"""
<jupyter_output>
(4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
<jupyter_text>
Q2:
<jupyter_code>
