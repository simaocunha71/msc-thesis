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

# Test the function.
assert parabola_directrix(5,3,2) == -198

# Further testing.
print(parabola_directrix(2, 0, 0))
print(parabola_directrix(3, 1, -1))
print(parabola_directrix(-2, -2, 3))
print(parabola_directrix(4, 3, 4))
print(parabola_directrix(4, -3, 4))

"""
(0, -198)
(1, -2)
(-8, 3)
(17, 8)
(-17, 8)
"""






































































































































































































































