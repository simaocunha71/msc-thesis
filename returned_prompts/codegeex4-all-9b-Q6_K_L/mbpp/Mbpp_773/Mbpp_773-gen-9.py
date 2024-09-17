def occurance_substring(string: str, substring: str) -> tuple:
  if substring in string:
    pos = string.index(substring)
    return (substring, pos, pos+len(substring))
  else:
    return None

