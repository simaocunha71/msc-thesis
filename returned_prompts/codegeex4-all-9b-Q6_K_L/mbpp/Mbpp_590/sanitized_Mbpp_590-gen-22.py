import cmath
def polar_rect(r: float, theta: float) -> tuple:
  x = r * cmath.cos(theta)
  y = r * cmath.sin(theta)
  return x, y