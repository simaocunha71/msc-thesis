def find_Rotations(s):
  return len(s) - len(set(s))
  # for i in range(1, len(s)):
  #   if s[i:] + s[:i] == s:
  #     return i
  # return len(s)