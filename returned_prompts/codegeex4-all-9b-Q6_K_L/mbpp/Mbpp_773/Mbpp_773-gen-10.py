def occurance_substring(s1: str,s2: str):
  try:
    pos = s1.index(s2)
    return (s2, pos, pos+len(s2))
  except ValueError:
    return None

