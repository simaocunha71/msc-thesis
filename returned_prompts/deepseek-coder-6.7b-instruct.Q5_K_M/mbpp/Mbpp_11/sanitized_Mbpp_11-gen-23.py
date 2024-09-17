def remove_Occ(s, c):
  s = list(s)
  s.remove(c)
  s = [i for i in s if i != c]
  return ''.join(s)