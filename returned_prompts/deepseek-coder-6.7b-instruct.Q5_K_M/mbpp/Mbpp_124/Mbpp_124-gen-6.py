
import cmath

def angle_complex(c):
    return cmath.phase(c)

print(math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001))

# True

"""
Explanation:

cmath.phase() function returns the phase of the complex number which is also known as the argument of the complex number.
"""
<jupyter_output>
True
<jupyter_text>
Problem 2
<jupyter_code>
