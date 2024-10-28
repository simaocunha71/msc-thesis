
from math import factorial as f
def count_binary_seq(n: int) -> float:
  return f(2 * n) / f(n + 1) / f(n)


