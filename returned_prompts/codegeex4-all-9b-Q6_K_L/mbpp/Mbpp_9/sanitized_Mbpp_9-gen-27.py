def find_Rotations(s: str) -> int:
  n = len(s)
  for i in range(1, n):
    temp = s[i:] + s[:i]
    if temp == s:
      return i
  return 1