def remove_Occ(s, c):
  s = s.replace(c, '', 1)
  return s[::-1].replace(c, '', 1)[::-1]