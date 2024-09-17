def sum_Of_Subarray_Prod(lst):
    """
    Returns the sum of products of all possible sublists of a given list
    """
    return sum([reduce(lambda a, b: a*b, lst[i:j+1]) for i in xrange(len(lst)) for j in xrange(i, len(lst))])