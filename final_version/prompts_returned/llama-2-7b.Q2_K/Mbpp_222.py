"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""

def check_type(tuple):
    return len(set(tuple[0])) == 1 and \
           isinstance(tuple[0], list)

print(check_type C[0:])