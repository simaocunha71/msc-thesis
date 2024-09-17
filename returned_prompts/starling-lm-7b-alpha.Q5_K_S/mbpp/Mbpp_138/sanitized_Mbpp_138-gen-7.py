def is_Sum_Of_Powers_Of_Two(n):
    """
    Returns True if the given number can be represented as a sum of non-zero powers of 2,
    False otherwise.
    """
    while n:
        if n % 2 == 0:
            return False
        n //= 2
    return True