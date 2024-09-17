
def remove_Occ(s, ch):
  first_occur = s.find(ch)
  if first_occur != -1:
    s = s[:first_occur] + s[first_occur+1:]
    last_occur = s.rfind(ch)
    if last_occur != -1:
      s = s[:last_occur] + s[last_occur+1:]
  return s


