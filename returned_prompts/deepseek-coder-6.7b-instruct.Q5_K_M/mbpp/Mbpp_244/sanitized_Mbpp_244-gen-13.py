import math
def next_Perfect_Square(n):
  root = math.sqrt(n)
  if int(root + 0.5) ** 2 == n:
    return n
  else:
    return (int(root)+1) ** 2