def parabola_directrix(a, h, k):
    """
    Find the directrix of a parabola.

    Parameters:
        a (float): The coefficient of the x^2 term in the equation.
        h (float): The horizontal shift of the parabola.
        k (float): The vertical shift of the parabola.

    Returns:
        float: The equation of the directrix.
    """
    return -1/a * h**2 + k