def find_Rotations(s):
  for i in range(1, len(s)):
    rotated_string = s[i:] + s[:i]
    if rotated_string == s:
      return i
  return -1