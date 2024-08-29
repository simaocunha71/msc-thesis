def angle_complex(z):
    return cmath.phase(z)

z = complex(0,1)
print(angle_complex(z))

"""
The function `cmath.phase(z)` returns the phase of the complex number `z` in radians.
The phase is the argument of the complex number.
"""

# Test
import math
assert math.isclose(angle_complex(0+1j), 1.5707963267948966, rel_tol=0.001)
assert math.isclose(angle_complex(1+1j), 1.2490457723982587, rel_tol=0.001)
assert math.isclose(angle_complex(1+0j), 0, rel_tol=0.001)
assert math.isclose(angle_complex(-1+0j), 3.141592653589793, rel_tol=0.001)
<jupyter_output>
1.5707963267948966
<jupyter_text>
1.2.3.3: Find the phase of a complex numberWrite a function to get the phase of a complex number.
<jupyter_code>
# Solution

