def set_left_most_unset_bit(n):
  return n | (1 << (bin(n)[2:].index('0') - 1))