def centered_hexagonal_number(n):
    """
    Finds the nth centered hexagonal number.

    A centered hexagonal number is a figurate number that represents a hexagon with a dot in the center and all other dots surrounding the center dot in a hexagonal lattice.
    
    The formula for the nth centered hexagonal number is given by:
    
    H_n = n * (2n - 1)

    Parameters:
    n (int): The position of the centered hexagonal number to find.

    Returns:
    int: The nth centered hexagonal number.
    """
    return n * (2 * n - 1)