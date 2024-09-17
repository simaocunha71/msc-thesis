def find_length(binary_str: str) -> int:
  max_diff = 0
  for i in range(len(binary_str)):
    for j in range(i, len(binary_str)):
      curr_str = binary_str[i:j+1]
      num_of_zeros = curr_str.count("0")
      num_of_ones = curr_str.count("1")
      diff = abs(num_of_zeros - num_of_ones)
      max_diff = max(max_diff, diff)
  return max_diff