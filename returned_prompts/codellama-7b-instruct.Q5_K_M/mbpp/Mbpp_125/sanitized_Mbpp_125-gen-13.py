def find_length(binary_str: str) -> int:
  count = 0
  for char in binary_str:
    if char == '0':
      count += 1
    else:
      count = 0
    if count > 6:
      return count
  return count