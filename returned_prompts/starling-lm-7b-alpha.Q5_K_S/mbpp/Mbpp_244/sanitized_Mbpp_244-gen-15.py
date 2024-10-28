import math
def next_Perfect_Square(n: int) -> int:
  if n % 2 == 0:
    while True:
      if math.sqrt(n) == int(math.sqrt(n)):
        return n
      n += 1
  else:
    while True:
      if math.sqrt(n) == int(math.sqrt(n)):
        return n
      n += 2