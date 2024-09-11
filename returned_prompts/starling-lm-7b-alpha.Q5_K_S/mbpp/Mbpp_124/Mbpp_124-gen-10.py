"""
The function `angle_complex` calculates the angle of a complex number.
The angle is calculated as the arctangent of the imaginary part divided by the real part.
The imaginary part is always positive, so the arctangent of a positive number returns a number in the range of 0 to pi.
"""

from math import atan

def angle_complex(x, y):
    return atan(y / x)

# Assert
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)

"""
The function `angle_complex` is a straightforward implementation of the arctangent function.
The arctangent function is defined as the angle whose tangent is a given number.
For example, if the tangent of an angle is 1/2, then the angle is pi/6, or 30 degrees.
The arctangent function is defined as the angle whose tangent is a given number, and the result is in radians.
The arctangent function is defined as the angle whose tangent is a given number, and the result is in degrees.
The arctangent function is defined as the angle whose tangent is a given number, and the result is in radians.
The arctangent function is defined as the angle whose tangent is a given number, and the result is in radians.
The arctangent function is defined as the angle whose tangent is a given number, and the result is in radians.
"""

"""
In mathematics, the arctangent function is defined as the angle whose tangent is a given number.
For example, if the tangent of an angle is 1/2, then the angle is pi/6, or 30 degrees.
The arctangent function is defined as the angle whose tangent is a given number, and the result is in radians.
The arctangent function is defined as the angle whose tangent is a given number, and the result is in degrees.
"""

"""
In the complex number system, the angle of a complex number is defined as the angle whose tangent is the imaginary part divided by the real part