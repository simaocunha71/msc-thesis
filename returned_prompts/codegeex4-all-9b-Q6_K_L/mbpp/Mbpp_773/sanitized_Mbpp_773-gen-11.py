def occurance_substring(string: str, substring: str) -> tuple:
  if substring in string:
    pos = string.index(substring)
    length = len(substring)
    return substring, pos, length
  else:
    return None