def occurance_substring(string: str, substring: str):
  if substring in string:
    return substring, string.find(substring), string.rfind(substring)
  else:
    return None

