def occurance_substring(string: str, substring: str):
  if substring in string:
    position = string.find(substring)
    return substring, position, len(substring)
  else:
    return None