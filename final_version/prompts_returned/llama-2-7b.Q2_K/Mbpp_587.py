"""
Write a function to convert a list to a tuple.
assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
"""

def list_to_tuple(list):
    return tuple(sorted(list))  

print(list_to_tuple([5,10,7,15,4]))