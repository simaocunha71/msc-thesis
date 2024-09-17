def occurance_substring(string: str, sub: str) -> tuple:
  if sub in string:
    return sub, string.index(sub), string.index(sub)+len(sub)
  return None