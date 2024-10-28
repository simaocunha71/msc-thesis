def all_unique(lst):
    """
    This function will return True if all the elements of a given list are unique and False otherwise

    Parameters:
    lst(list): The list of integers

    Returns:
    bool: True if all the elements of the list are unique, False if not
    """
    seen = set()
    for elem in lst:
        if elem in seen:
            return False
        seen.add(elem)
    return True