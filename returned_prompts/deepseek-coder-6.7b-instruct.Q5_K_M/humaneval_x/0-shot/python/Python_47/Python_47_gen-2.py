
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]


# Test cases
print(median([3, 1, 2, 4, 5]))  # 3
print(median([-10, 4, 6, 1000, 10, 20]))  # 15.0

# Alternative solution

def median_alt(l: list):
    """Return median of elements in the list l.
    >>> median_alt([3, 1, 2, 4, 5])
    [3]
    >>> median_alt([-10, 4, 6, 1000, 10, 20])
    [10, 20]
    """

    l.sort()
    n = len(l)
    if n % 2 == 0:
        return l[n//2 - 1:n//2]
    else:
        return [l[n//2]]


# Test cases
print(median_alt([3, 1, 2, 4, 5]))  # [3]
print(median_alt([-10, 4, 6, 1000, 10, 20]))  # [10, 20]

# Alternative solution

def median_alt(l: list):
    """Return median of elements in the list l.
    >>> median_alt([3, 1, 2, 4, 5])
    [3]
    >>> median_alt([-10, 4, 6, 1000, 10, 20])
    [10, 20]
    """

    l.sort()
    n = len(l)
    if n % 2 == 0:
        return l[n//2 - 1:n//2]
    else:
        return [l[n//2]]

