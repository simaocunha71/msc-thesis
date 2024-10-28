def remove_Occ(s, c):
  return s[:s.find(c)] + s[s.rfind(c)+1:]