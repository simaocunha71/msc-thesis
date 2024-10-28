import doctest
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