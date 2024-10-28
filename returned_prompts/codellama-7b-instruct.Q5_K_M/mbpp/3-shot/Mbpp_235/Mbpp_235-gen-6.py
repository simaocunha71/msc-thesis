
def even_bit_set_number(num: int) -> int:
  num &= 0xaaaaaaaa
  return num


