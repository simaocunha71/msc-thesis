import math
def is_perfect_square(n):
    """
    Args:
        n (int): The number to check.
    Returns:
        bool: True if the number is a perfect square, False otherwise.
    """
    sqrt = math.sqrt(n)
    return sqrt % 1 == 0