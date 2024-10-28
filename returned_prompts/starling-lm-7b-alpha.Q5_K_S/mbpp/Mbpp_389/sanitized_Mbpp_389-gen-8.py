def find_lucas(n):
    """
    Find the n'th lucas number.
    Time complexity: O(log(n))
    """
    if n == 0:
        return 2
    if n == 1:
        return 1

    a, b = 2, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a