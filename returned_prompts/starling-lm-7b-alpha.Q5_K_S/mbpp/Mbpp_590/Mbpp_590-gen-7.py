
import cmath
def polar_rect(r, theta):
    return (r * cmath.exp(complex(0, theta)), r * cmath.exp(complex(math.pi, theta)))


