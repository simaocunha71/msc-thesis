
def is_undulating(n):
  s1 = str(n)
  s2 = str(n)[::-1]
  return ''.join(s1) == ''.join(s2)


