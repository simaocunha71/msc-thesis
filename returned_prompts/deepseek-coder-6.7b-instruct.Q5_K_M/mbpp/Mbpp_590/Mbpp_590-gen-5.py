
import cmath
def polar_rect(rho, theta):
    return cmath.rect(rho * cmath.cos(theta), rho * cmath.sin(theta)), cmath.exp(1j * theta)
"""
cmath.rect(rho * cmath.cos(theta), rho * cmath.sin(theta)) converts polar to rectangular.
cmath.exp(1j * theta) returns the complex number with given phase angle.
"""

