def centered_hexagonal_number(n):
    """
    Calculate the nth centered hexagonal number.

    A centered hexagonal number is a centered figurate number that represents a hexagon with a dot in the center and all other dots surrounding the center dot in a hexagonal lattice.

    The formula for the nth centered hexagonal number is given by: H(n) = n * (2n - 1)

    :param n: The position of the centered hexagonal number in the sequence.
    :return: The nth centered hexagonal number.
    """
    return n * (2 * n - 1)