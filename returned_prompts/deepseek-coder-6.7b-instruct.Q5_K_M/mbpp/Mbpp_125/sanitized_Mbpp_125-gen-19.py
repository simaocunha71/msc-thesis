def find_length(s: str) -> int:
  cnt0, cnt1, max_len = [0]*3
  for i in range(len(s)):
    if s[i] == '0':
      cnt0 += 1
    else:
      cnt1 += 1
    if cnt0 == cnt1:
      max_len = max(max_len, cnt0*2)
  return max_len