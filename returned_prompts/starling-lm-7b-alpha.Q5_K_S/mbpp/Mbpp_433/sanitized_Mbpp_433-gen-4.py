import doctest
def check_greater(arr, num):
    """
    Checks whether the entered number is greater than the elements of the given array
    >>> check_greater([1, 2, 3, 4, 5], 4)
    False
    """
    return num > max(arr)