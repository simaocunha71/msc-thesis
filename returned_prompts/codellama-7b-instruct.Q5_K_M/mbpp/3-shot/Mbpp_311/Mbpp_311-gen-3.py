
def set_left_most_unset_bit(n):
  n |= n-1
  return n+1


