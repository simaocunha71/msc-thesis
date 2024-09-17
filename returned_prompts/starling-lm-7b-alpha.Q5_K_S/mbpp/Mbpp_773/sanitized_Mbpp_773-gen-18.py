def occurance_substring(str: str, sub: str) -> tuple:
  start_index = str.find(sub)
  if start_index == -1:
    return None
  else:
    return (sub, start_index, start_index + len(sub))