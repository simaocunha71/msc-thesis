
def find_length(binary_string: str) -> int:
  count_ones = 0
  count_zeros = 0
  max_diff = 0
  for char in binary_string:
    if char == "1":
      count_ones += 1
    else:
      count_zeros += 1
    max_diff = max(max_diff, abs(count_ones - count_zeros))
  return max_diff


