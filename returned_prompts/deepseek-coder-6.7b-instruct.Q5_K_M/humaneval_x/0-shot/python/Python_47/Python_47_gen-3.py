
    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
"""

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l.sort()
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test cases
print(median([3, 1, 2, 4, 5]))  # should return 3
print(median([-10, 4, 6, 1000, 10, 20]))  # should return 15.0

# Test cases
print(median([3, 1, 2, 4, 5]))  # should return 3
print(median([-10, 4, 6, 1000, 10, 20]))  # should return 15.0
<jupyter_output>
3
15.0
3
15.0
<jupyter_text>
Test Cases
<jupyter_code>
# Test cases
print(median([3, 1, 2, 4, 5]))  # should return 3
print(median([-10, 4, 6, 1000, 10, 20]))  # should return 15.0

# Test cases
print(median([3, 1, 2, 4, 5]))  # should return 3
print(median([-10, 4, 6, 1000, 