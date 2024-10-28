def union_elements(tup1, tup2):
    return tuple(sorted(set(tup1 + tup2)))  # using set to remove duplicates and sorted to sort in ascending order