def union_elements(tup1, tup2):
    # Use set to get unique elements from both tuples
    unique_elements = set(tup1).union(set(tup2))
    # Convert the set back to a sorted tuple
    return tuple(sorted(unique_elements))