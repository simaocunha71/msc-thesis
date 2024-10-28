def occurance_substring(s: str, sub: str) -> tuple:
  index = s.find(sub)
  if index != -1:
    return (sub, index, index+len(sub))
  return None