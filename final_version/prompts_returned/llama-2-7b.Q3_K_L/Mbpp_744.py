"""
Write a function to check if the given tuple has any none value or not.
assert check_none((10, 4, 5, 6, None)) == True
"""

def check_none(tuple):
    for i in range(len(tuple)):
        if tuple[i] is None:
            return False
        
    return True