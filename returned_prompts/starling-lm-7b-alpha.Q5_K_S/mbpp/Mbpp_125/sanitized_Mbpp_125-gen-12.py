def find_length(binary_string: str) -> int:
  max_length = 0
  for i in range(len(binary_string)):
    for j in range(i, len(binary_string)):
      if binary_string[i] == '0' and binary_string[j] == '1':
        max_length = max(max_length, j - i + 1)
  return max_length