"""
Write a function to join a list of multiple integers into a single integer.
assert multiple_to_single([11, 33, 50])==113350
"""

def multiple_to_single(list_of_integers):
    # your code goes here
    
    return sum(i for i in list_of_integers)