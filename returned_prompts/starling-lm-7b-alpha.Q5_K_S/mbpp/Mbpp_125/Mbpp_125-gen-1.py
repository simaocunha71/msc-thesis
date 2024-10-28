
def find_length(s: str) -> int:
  max_len = 0
  for i in range(len(s)):
    max_len = max(max_len, s.count("0") + s[:i].count("1") + s[i+1:].count("1"))
  return max_len


