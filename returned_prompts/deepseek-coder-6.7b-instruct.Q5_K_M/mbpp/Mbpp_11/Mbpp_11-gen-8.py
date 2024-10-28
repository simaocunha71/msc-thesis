
def remove_Occ(s: str, ch: str) -> str:
  first_Occ = s.find(ch)
  last_Occ = s.rfind(ch)
  if first_Occ != -1 and last_Occ != -first_Occ:
    s = s[:first_Occ] + s[first_Occ+1:last_Occ] + s[last_Occ+1:]
  return s


