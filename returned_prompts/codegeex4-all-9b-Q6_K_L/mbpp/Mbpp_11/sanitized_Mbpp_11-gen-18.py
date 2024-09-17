def remove_Occ(s, c):
  return s[:s.index(c)] + s[s.index(c) + 1: -s[::-1].index(c) - 1] + s[-s[::-1].index(c):]