def second_smallest(lst):
    """
    Return the second smallest number in a list.

    Parameters
    ----------
    lst : list
        A list of numbers.

    Returns
    -------
    smallest : int
        The second smallest number in the list.
    """
    lst.sort()
    return lst[1]


# Test the function
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2


# More tests
print(second_smallest([2, 3, 4, 5, 6])) # 3
print(second_smallest([-1, -2, -3, -4, -5])) # -2
print(second_smallest([1, -2, -2])) # -2
print(second_smallest([-1, -1, -2])) # -2
print(second_smallest([-2, -2, -2])) # -2
print(second_smallest([-2, -2, 0])) # 0
print(second_smallest([0, -2, -2])) # 0
print(second_smallest([-2, 0, 0])) # 0
print(second_smallest([0, 0, 0])) # 0
print(second_smallest([-2, 0, -2])) # 0
print(second_smallest([0, -2, 0])) # 0
print(second_smallest([-2, 0, -1])) # 0


def second_smallest(lst):
    """
    Return the second smallest number in a list.

    Parameters
    ----------
    lst : list
        A list of numbers.

    Returns
    -------
    smallest : int
        The second smallest number in the list.
    """
    lst.sort()
    return lst[1]


# Test the function
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2


# More tests
print(second_smallest([2, 3, 4, 5