import math
def is_perfect_square(n):
  root = math.sqrt(n)
  return int(root + 0.5) ** 2 == n

