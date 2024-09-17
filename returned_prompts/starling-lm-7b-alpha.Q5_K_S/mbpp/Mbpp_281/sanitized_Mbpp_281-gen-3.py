def all_unique(lst):
    """
    Check if all elements of a given list are unique
    """
    if len(lst) == len(set(lst)):
        return True
    else:
        return False