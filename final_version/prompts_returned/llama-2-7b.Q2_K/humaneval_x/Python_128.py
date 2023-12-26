
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    # check if arr is empty
    if len(arr) < 3: return None

    # get product of all signs in the array
    # if the array doesn't contain any number, then we will be returning None
    # else, the product is returned
    product = [1, -1][:][arr[:]].count(1) * arr[:]
    return float(product)
