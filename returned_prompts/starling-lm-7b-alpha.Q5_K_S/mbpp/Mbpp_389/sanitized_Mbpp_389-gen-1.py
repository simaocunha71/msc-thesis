def find_lucas(n):
    """
    Find the n'th lucas number.

    Time complexity: O(log n)
    Space complexity: O(1)
    """
    if n == 0:
        return 2
    if n == 1:
        return 1
    a = 2
    b = 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a