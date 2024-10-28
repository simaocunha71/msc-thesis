def check_distinct(tup):
    """
    Returns True if the given tuple contains no duplicates, otherwise False
    """
    return len(tup) == len(set(tup))