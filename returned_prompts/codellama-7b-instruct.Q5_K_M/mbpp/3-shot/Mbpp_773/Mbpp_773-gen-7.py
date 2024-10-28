
def occurance_substring(string: str,substring: str) -> tuple:
  match = string.find(substring)
  if match == -1:
    return None
  return substring, match, match + len(substring)


