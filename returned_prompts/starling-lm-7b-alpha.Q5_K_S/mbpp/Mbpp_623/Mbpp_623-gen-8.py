def nth_nums(lst, n):
    """
    Compute the n-th power of each number in a list.

    >>> nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2)
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    return [num ** n for num in lst]


# Test cases
assert nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# More test cases
assert nth_nums([1, 0, 0, -1], 0) == [1, 0, 0, 1]
assert nth_nums([-3, -2, -1, 0, 1], 3) == [-27, -8, -1, 0, 1]
assert nth_nums([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5], 2) == [2.25, 6.25, 12.25, 20.25, 28.25, 36.25, 44.25, 52.25, 60.25, 68.25]

# Test with empty list
assert nth_nums([], 2) == []

# Test with single element
assert nth_nums([1], 2) == [1]

# Test with negative number
assert nth_nums([-1], 2) == [-1]

# Test with zero
assert nth_nums([