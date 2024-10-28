
import cmath
def polar_rect(rho: float, theta: float) -> tuple:
  rect_coordinates = (rho*cmath.cos(theta), rho*cmath.sin(theta))
  return rect_coordinates


