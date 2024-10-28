def combinations_list(lst):
    """Find all possible combinations of the elements of a given list."""
    result = [[]]
    for item in lst:
        result += [[item] + x for x in result]
    return result