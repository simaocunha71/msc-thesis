
def odd_Equivalent(binary_str: str, times: int) -> int:
  rotated_str = binary_str[times:] + binary_str[:times]
  return rotated_str.count("1")


