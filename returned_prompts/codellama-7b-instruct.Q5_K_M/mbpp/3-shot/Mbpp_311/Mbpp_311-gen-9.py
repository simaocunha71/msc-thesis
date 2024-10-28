
def set_left_most_unset_bit(n):
  n |= (n - 1) & n
  return n


