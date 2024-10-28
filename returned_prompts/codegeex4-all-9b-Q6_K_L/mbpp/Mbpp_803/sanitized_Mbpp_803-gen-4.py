def is_perfect_square(n: int) -> bool:
    """
    Check if the given number is a perfect square.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if n is a perfect square, False otherwise.
    """
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n