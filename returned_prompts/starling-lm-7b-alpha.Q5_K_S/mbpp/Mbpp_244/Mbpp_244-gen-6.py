
import math
def next_Perfect_Square(n: int) -> int:
  if n % 2 == 0:
    n += 1
  while math.sqrt(n).is_integer() == False:
    n += 1
  return n


