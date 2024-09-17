def find_Rotations(s: str) -> int:
  if len(s) == 1:
    return 1
  for i in range(1, len(s)):
    if s == s[i:] + s[:i]:
      return i
  return -1