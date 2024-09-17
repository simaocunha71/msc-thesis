
def find_Rotations(s: str) -> int:
  for i in range(1, len(s)):
    if s[i:] + s[:i] == s:
      return i
  return len(s)


