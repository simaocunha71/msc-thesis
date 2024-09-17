
def remove_Occ(s,c):
  f = s.find(c)
  if f != -1:
    s = s[:f] + s[f+1:]
    f = s.rfind(c)
    if f != -1:
      s = s[:f] + s[f+1:]
  return s


