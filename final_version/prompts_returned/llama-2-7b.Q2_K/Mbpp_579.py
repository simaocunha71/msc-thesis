"""
Write a function to find the dissimilar elements in the given two tuples.
assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
"""

def find_dissimilar(tuple1, tuple2):
    """Returns a dictionary of differences.
    The key is the elements in the first tuple
    and the value is that element's index in the second tuple.
    If there are no differences then return an empty dictionary."""
    
    # Find which index numbers correspond to different values between tuples
    dissimilar_elements = {}
    
    for item1, item2 in zip(tuple1, tuple2):
        if item1 != item2:
            indices[item1] = (item1, len(tuple2))
            
    return dissimilar_elements
