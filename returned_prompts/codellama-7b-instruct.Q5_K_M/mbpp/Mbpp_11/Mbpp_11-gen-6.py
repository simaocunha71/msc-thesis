
def remove_Occ(s,c):
  first = s.find(c)
  last = s.rfind(c)
  return s[:first] + s[last+1:]


