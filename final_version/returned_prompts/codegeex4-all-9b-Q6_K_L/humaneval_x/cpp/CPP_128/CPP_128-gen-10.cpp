def prod_signs(arr):
    """
    You are given a vector arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the vector, represented by 1, -1 or 0.
    Note: return -32768 for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == -32768
    """
    return -32768 if not arr else sum(abs(i) * (-1 if i < 0 else 1) for i in arr)

