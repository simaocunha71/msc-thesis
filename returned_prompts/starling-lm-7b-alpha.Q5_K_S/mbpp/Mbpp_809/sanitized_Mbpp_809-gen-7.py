def check_smaller(t1, t2):
    """
    Check if each element of second tuple is smaller than its corresponding element in the first tuple.
    """
    return all(a < b for a, b in zip(t1, t2))