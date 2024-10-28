def odd_Equivalent(binary_string: str, rotations: int) -> int:
  odd_count = 0
  for i in range(rotations):
    rotated_string = binary_string[-1] + binary_string[:-1]
    if int(rotated_string, 2) % 2 == 1:
      odd_count += 1
    binary_string = rotated_string
  return odd_count