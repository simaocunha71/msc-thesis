
import math
def next_Perfect_Square(num: int) -> int:
  x = int(math.sqrt(num))
  while (x+1)**2 <= num:
    x += 1
  return x**2


