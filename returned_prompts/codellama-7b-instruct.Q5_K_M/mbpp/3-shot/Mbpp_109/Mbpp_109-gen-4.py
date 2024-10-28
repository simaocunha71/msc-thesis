
def odd_Equivalent(binary_string: str, num_rotations: int) -> int:
  rotated_binary = binary_string[num_rotations:] + binary_string[:num_rotations]
  num_of_odd_vals = rotated_binary.count("1")
  return num_of_odd_vals


