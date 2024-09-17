def find_length(binary_str: str) -> int:
  count_0 = binary_str.count("0")
  count_1 = binary_str.count("1")
  max_diff = max(count_0, count_1) - min(count_0, count_1)
  return max_diff