def find_length(s: str) -> int:
  max_diff = 0
  cur_diff = 0
  for ch in s:
    if ch == '0':
      cur_diff += 1
    else:
      cur_diff -= 1
    if cur_diff > max_diff:
      max_diff = cur_diff
  return max_diff