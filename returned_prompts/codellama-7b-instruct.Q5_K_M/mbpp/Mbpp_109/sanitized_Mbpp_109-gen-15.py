def odd_Equivalent(binary_str:str, num_rotations:int) -> int:
  rotated_binary = binary_str[-num_rotations:] + binary_str[:-num_rotations]
  return rotated_binary.count("1")