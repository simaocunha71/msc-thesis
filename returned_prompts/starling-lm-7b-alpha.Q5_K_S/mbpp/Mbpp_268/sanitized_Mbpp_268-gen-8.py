def find_star_num(n):
    """
    Find the n'th star number

    Parameters:
    n (int): The position of the star number

    Returns:
    int: The n'th star number
    """
    return 2 ** (2 * n + 1) - 1