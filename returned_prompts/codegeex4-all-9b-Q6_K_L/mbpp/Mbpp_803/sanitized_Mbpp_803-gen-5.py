def is_perfect_square(n):
    """
    Check if the given number is a perfect square.

    :param n: int, the number to check
    :return: bool, True if n is a perfect square, False otherwise
    """
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n