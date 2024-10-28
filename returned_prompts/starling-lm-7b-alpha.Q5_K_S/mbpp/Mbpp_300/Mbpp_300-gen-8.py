
from math import comb
def count_binary_seq(n: int) -> int:
  return 2 * comb(2*n, n)


