def check_none(tup):
    """
    Check if the given tuple has any none value or not.

    Parameters:
    tup (tuple): The given tuple.

    Returns:
    bool: True if the tuple has any none value, False otherwise.
    """
    for elem in tup:
        if elem is None:
            return True
    return False