
def find_Rotations(s: str) -> int:
  return len([1 for i in range(1, len(s)) if s[i:]+s[:i] == s])


