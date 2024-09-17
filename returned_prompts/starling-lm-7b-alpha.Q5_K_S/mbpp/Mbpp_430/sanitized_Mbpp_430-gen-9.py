def parabola_directrix(a, b, c):
    """
    Function to find the directrix of a parabola.

    Parameters:
        a (int): coefficient of x^2
        b (int): coefficient of x
        c (int): constant

    Returns:
        int: the directrix of the parabola
    """
    # calculate the directrix
    directrix = -c / a

    # return the directrix
    return directrix