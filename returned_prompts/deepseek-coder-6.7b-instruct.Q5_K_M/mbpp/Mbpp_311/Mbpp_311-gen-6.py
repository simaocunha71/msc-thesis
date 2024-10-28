
def set_left_most_unset_bit(n):
  return n | (1<<n.bit_length())


