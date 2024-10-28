
def occurance_substring(s: str, sub: str) -> tuple:
  start = s.find(sub)
  if start == -1:
    return None
  end = start + len(sub)
  return (sub, start, end)


