"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""

def is_sublist(a, b):
    if len(a) == len(b):
        for i in range(len(b)):
            if a[i] != b[i]: return False
    else:
        print("The length of the two lists are not equal")
    return True