"""
Write a function to get the angle of a complex number.
assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
"""
import math
from typing import Union

def angle_complex(z: Complex[float]) -> float:
    """
    A function to get the angle of a complex number by calculating
    the argument using the Euler's identity.
    
    :param z: The input complex number
    :type z: Union[str, Complex[float]]
    
    :return: 2*pi*angle_complex(z) where pi = -3.14
    """
    if type(z) == str and 'i' in z:
        return math.atan((z[-1] * 0 if '-' not in z else 1j))
    elif type(z) == str and 'j' in z:
        return math.asin((z[1] * 0 if '-' not in z else 1j))
        
    c = Complex(z, 0)
    
    return math.atan2((c[1], -c[0]))
