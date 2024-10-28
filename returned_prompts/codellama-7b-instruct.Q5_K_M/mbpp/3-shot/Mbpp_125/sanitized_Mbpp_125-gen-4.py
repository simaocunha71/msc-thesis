def find_length(binary_string: str) -> int:
  count_0 = binary_string.count('0')
  count_1 = binary_string.count('1')
  return abs(count_0 - count_1)