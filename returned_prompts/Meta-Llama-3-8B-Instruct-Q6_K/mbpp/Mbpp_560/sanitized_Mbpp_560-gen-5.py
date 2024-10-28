def union_elements(test_tup1, test_tup2):
    return tuple(sorted(set(test_tup1 + test_tup2)))  # Convert to set to remove duplicates, then back to tuple, and finally sort