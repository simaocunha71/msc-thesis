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

    def is_unique(n):
        """Return True if n has no even digits, False otherwise."""
        return all(int(digit) % 2 != 0 for digit in str(n))

    return sorted([n for n in x if is_unique(n)])

print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))