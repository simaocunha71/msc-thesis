def find_length(s: str) -> int:
  max_length = 0
  for i in range(len(s)):
    cnt = 0
    for j in range(i, len(s)):
      if s[j] == '0':
        cnt += 1
      else:
        cnt -= 1
      max_length = max(max_length, cnt)
  return max_length