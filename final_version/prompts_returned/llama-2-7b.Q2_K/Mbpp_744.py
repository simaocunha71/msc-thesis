"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(tup):
    for i in tup:
        if isinstance(i, TypeError) and i.args[0] == 'NoneType': #check to see if the tuple has any none value or not.
            return True
    return False