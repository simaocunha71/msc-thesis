
import cmath
def polar_rect(r, theta):
  return cmath.rect(r * cmath.cos(theta), r * cmath.sin(theta)), cmath.exp(1j * theta)


