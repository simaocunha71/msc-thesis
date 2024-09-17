
from math import sqrt
def triangle_area(radius: float) -> float:
  if radius < 0:
    return None
  semi_perimeter = sqrt(radius**2 * 2)
  area = (semi_perimeter*(semi_perimeter-radius)*(semi_perimeter-radius))**0.5
  return area


