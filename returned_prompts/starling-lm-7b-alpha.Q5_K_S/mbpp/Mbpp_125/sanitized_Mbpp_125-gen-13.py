def find_length(binary_string: str) -> int:
  length = 0
  for i in range(len(binary_string)):
    if binary_string[i] == '0':
      length = max(length + 1, 1)
    else:
      length += 1
  return length