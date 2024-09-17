def even_bit_set_number(n: int) -> int:
  mask = 0b10101010101010101010101010101010
  return n | mask