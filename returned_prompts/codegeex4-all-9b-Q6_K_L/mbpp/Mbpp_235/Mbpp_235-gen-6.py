def even_bit_set_number(num: int) -> int:
  # Create a mask with even bits set to 1
  mask = 0b01010101010101010101010101010101
  # Apply the mask to the number
  result = num | mask
  return result

