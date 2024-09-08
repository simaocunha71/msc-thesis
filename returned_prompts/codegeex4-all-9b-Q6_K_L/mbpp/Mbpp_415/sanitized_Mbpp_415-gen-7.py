def max_Product(lst):
    """
    Find a pair with highest product from a given array of integers.

    >>> max_Product([1,2,3,4,7,0,8,4])
    (7, 8)
    """
    # Sort the list in descending order
    lst.sort(reverse=True)
    # Return the first two elements of the list
    return (lst[0], lst[1])