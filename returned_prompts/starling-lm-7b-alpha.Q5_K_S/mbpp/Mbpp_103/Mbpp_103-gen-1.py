"""
def eulerian_num(n, m):
    """
    Find the Eulerian number a(n, m).
    >>> eulerian_num(3, 1)
    4
    """
    # Create a memoization dictionary
    memo = {(n, m): 0}

    def eulerian(n, m):
        # Base case
        if n == 1:
            return m == 0
        # Recursive case
        if (n, m) not in memo:
            memo[n, m] = eulerian(n - 1, m - 1) + m * eulerian(n - 1, m)
        return memo[n, m]

    return eulerian(n, m)
"""
def eulerian_num(n, m):
    """
    Find the Eulerian number a(n, m).
    >>> eulerian_num(3, 1)
    4
    """
    # Create a memoization dictionary
    memo = {(n, m): 0}

    def eulerian(n, m):
        # Base case
        if n == 1:
            return m == 0
        # Recursive case
        if (n, m) not in memo:
            memo[n, m] = eulerian(n - 1, m - 1) + m * eulerian(n - 1, m)
        return memo[n, m]

    return eulerian(n, m)

# Make sure the above function works correctly.
import doctest
if doctest.testmod() != 0:
    print('Some doctests failed')
else:
    print('All doctests passed')

# Test the above function.
print(eulerian_num(3, 1))  # Should print: 4

# Test the above function with different inputs.
for n in range(1, 5):
    for m in range(n + 1):
        assert eulerian_num(n, m) == eulerian(n, m)
        assert eulerian_num(n, m) ==