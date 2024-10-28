
def odd_Equivalent(binary_str: str, num_rotations: int) -> int:
  if num_rotations == 0:
    return sum(int(x) for x in binary_str)
  else:
    return sum(int(x) for x in binary_str[num_rotations:] + binary_str[:num_rotations])


