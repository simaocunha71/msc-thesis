def centered_hexagonal_number(n):
    """
    Returns the nth centered hexagonal number.

    A centered hexagonal number is a figurate number that represents a hexagon
    with a dot in the center and all other dots surrounding the center dot in a
    hexagonal lattice.

    The formula for the nth centered hexagonal number is given by:
    H_n = (3n^2 - 3n + 2) / 2

    >>> centered_hexagonal_number(10)
    271
    """
    return (3 * n * n - 3 * n + 2) // 2