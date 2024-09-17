def list_split(lst,n):
    """
    Splits a list for every nth element, returning a list of the resulting lists.
    """
    return [lst[i::n] for i in range(n)]