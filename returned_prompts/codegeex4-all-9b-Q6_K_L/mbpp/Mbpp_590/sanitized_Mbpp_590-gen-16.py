import math
def polar_rect(rho: float, theta: float) -> tuple:
  x = rho * math.cos(theta)
  y = rho * math.sin(theta)
  return (x, y)