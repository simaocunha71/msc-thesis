"""
Write a function to find the volume of a sphere.
assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
"""

import numpy as np
from scipy import optimize

def volume_cylinder(rad):
    return np.pi * (rad ** 2) ** 2 / 3
    
def volume_sphere(radius):
    return (4/3)*np.pi*radius**3


if __name__ == "__main__":
    import sys

    # Get input and validate it
    if len(sys.argv) < 2:
        print("Usage: %s radius\n", sys.argv[0])
        sys.exit(-1)
    
    radius = float(sys.argv[1])

    assert volume_cylinder(radius) == volume_sphere(radius), "error"