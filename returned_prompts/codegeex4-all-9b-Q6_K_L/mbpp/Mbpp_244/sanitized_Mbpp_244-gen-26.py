import math
def next_Perfect_Square(n):
  sqrt = math.sqrt(n)
  if sqrt == int(sqrt):
    return int(sqrt+1)**2
  else:
    return int(sqrt+1)**2