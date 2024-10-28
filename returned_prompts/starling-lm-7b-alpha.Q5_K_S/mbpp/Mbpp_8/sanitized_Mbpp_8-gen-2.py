def square_nums(nums):
    """
    Find squares of individual elements in a list.

    >>> square_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    return [num ** 2 for num in nums]