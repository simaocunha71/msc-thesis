def cube_Sum(n):
    """
    Finds the cube sum of the first n even natural numbers.

    Args:
        n (int): The number of even natural numbers to be considered.

    Returns:
        int: The sum of cubes of the first n even natural numbers.
    """
    return sum([i**3 for i in range(2, 2 + n)])