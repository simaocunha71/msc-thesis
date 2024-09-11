import math
def is_polite(n):
    """Check if a number is polite"""
    return n == 2 * sum(x for x in range(1, n)) + n