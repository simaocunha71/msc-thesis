def remove_Occ(s: str, c: str) -> str:
  if s.count(c) < 2:
    return s
  else:
    s = s.replace(c, '', 1)
    s = s.replace(c, '', 1)
    return s