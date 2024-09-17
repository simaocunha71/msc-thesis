def find_length(binary_string: str) -> int:
  max_length = 0
  for i in range(len(binary_string)):
    cnt = 0
    for j in range(i, len(binary_string)):
      if binary_string[j] == '0':
        cnt += 1
      else:
        cnt -= 1
      max_length = max(max_length, cnt)
  return max_length