"""
Write a function to add a dictionary to the tuple. The output should be a tuple.
assert add_dict_to_tuple((4, 5, 6), {"MSAM" : 1, "is" : 2, "best" : 3} ) == (4, 5, 6, {'MSAM': 1, 'is': 2, 'best': 3})
"""
from typing import Optional

def add_dict_to_tuple(tuple: tuple, dict_: Optional[dict]) -> tuple:
    if not isinstance(tuple, tuple):
        print("ERROR! tuple should be a tuple")
        return tuple

    for key, value in dict_.items():
        tuple = tuple[0] + (dict_,)
    
    return tuple