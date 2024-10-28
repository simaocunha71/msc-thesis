import pytest
def find_star_num(n):
    """
    Finds the n'th star number.

    Parameters
    ----------
    n : int
        The position of the number.

    Returns
    -------
    int
        The n'th star number.
    """
    return 3 * n * (n + 1)