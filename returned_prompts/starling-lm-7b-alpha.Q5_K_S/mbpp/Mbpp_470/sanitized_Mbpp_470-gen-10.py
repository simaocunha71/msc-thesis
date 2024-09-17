def add_pairwise(tup):
    """
    This function will return a tuple of the sum of the neighboring elements of the given tuple.
    """
    result = []
    for i in range(len(tup)-1):
        result.append(tup[i]+tup[i+1])
    result.append(tup[len(tup)-1]+tup[0])
    return tuple(result)