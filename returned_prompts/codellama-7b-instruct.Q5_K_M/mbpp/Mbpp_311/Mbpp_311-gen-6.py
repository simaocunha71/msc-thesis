
def set_left_most_unset_bit(n: int) -> int:
  while (n & (n + 1)) != 0:
    n = n & (n + 1)
  return n + 1


