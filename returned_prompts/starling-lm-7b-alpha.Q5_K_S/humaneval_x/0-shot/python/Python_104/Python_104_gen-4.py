    from itertools import combinations

    def is_even(n):
        return any(int(i) % 2 == 0 for i in str(n))

    def is_odd(n):
        return not is_even(n)

    result = []
    for i in x:
        if not any(int(j) % 2 == 0 for j in str(i)):
            result.append(i)

    return result


# For testing purpose
print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []






def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    from itertools import combinations

    def is_even(n):
        return any(int(i) % 2 == 0 for i in str(n))

    def is_odd(n):
        return not is_even(n)

    result = []
    for i in x:
        if not any(int(j) % 2 == 0 for j in str(i)):
            result.append(i)

    return result


# For testing purpose
print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []









