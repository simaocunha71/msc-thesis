def is_Sum_Of_Powers_Of_Two(n):
    """
    This function checks whether the given number can be represented as sum of non-zero powers of 2 or not.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number can be represented as sum of non-zero powers of 2, False otherwise.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    while n > 0:
        if n % 2 != 0 and n != 1:
            return False
        n //= 2

    return True