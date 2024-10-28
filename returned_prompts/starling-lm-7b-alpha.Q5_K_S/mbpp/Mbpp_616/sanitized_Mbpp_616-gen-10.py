def tuple_modulo(tup1, tup2):
    """
    Takes two tuples of the same length and performs the element wise modulo.
    """
    return tuple(a % b for a, b in zip(tup1, tup2))