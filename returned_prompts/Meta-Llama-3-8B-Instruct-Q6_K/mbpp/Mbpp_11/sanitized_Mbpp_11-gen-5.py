def remove_Occ(s, c):
  return s[:s.index(c)] + s[s.index(c)+1:s.rindex(c)]