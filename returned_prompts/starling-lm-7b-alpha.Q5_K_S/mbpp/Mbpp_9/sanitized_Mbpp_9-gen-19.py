def find_Rotations(s: str) -> int:
  n = len(s)
  for i in range(n):
    if s[:i] == s[i:]:
      return i
  return n