
def is_undulating(n):
  s = str(n)
  for i in range(2, len(s)):
    if s[i-2] == s[i-1] or s[i-1] == s[i]:
      return False
  return True


