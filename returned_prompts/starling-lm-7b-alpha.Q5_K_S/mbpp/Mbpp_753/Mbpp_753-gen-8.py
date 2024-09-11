"""
Here is one way to solve this problem, by sorting the list and then returning the first k elements:

def min_k(tups, k):
    # Sort the list by the second item in the tuple, ascending
    sorted_tups = sorted(tups, key=lambda tup: tup[1])
    # Return the first k tuples
    return sorted_tups[:k]
"""

