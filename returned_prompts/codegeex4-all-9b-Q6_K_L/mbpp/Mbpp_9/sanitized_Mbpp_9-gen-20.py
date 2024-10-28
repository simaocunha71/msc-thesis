def find_Rotations(s: str) -> int:
  n = len(s)
  for i in range(1, n+1):
    if s[i:] + s[:i] == s:
      return i
  return -1