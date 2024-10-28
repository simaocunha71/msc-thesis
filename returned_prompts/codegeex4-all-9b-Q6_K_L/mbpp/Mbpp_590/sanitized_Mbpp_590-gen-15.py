import cmath
def polar_rect(rho, theta):
  x = rho * cmath.cos(theta)
  y = rho * cmath.sin(theta)
  return (x, y)