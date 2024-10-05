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

    def no_even_digits(n):
        """Return True if n has no even digit, False otherwise."""
        for digit in str(n):
            if int(digit) % 2 == 0:
                return False
        return True

    return sorted([num for num in x if no_even_digits(num)])

print(unique_digits([15, 33, 1422, 1]))
print(unique_digits([152, 323, 1422, 10]))