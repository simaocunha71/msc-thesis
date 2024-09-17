import cmath
def convert(num):
    """
    Convert a complex number to polar coordinates.

    Parameters:
    num (complex): The complex number to convert.

    Returns:
    (tuple): A tuple containing the magnitude and angle of the complex number.
    """
    magnitude = cmath.polar(num)[0]
    angle = cmath.polar(num)[1]

    return magnitude, angle