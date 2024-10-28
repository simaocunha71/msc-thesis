def odd_Equivalent(binary_str: str, n: int) -> int:
  binary_list = list(binary_str)
  binary_list_rotated = binary_list[n:] + binary_list[:n]
  count = 0
  for digit in binary_list_rotated:
    if int(digit) % 2 == 1:
      count += 1
  return count