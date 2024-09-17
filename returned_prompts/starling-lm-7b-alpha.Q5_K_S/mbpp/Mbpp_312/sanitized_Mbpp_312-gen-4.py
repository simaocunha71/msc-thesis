import math
import numpy as np
def volume_cone(r, h):
    """
    Function to find the volume of a cone.
    """
    # calculate the volume using the formula pi * r^2 * h / 3
    volume = math.pi * (r**2) * h / 3
    return volume