def remove_Occ(s: str, c: str) -> str:
  s = s.replace(c, "", 1)
  s = s[::-1].replace(c, "", 1)[::-1]
  return s