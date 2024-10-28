def occurance_substring(s: str, sub: str) -> tuple:
  pos = s.find(sub)
  if pos != -1:
    return (sub, pos, pos + len(sub))
  return None