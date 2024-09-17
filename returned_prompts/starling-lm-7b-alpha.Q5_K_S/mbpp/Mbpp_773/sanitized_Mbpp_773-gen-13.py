def occurance_substring(string: str, substring: str) -> tuple:
  if substring in string:
    return (substring, string.find(substring), string.find(substring)+len(substring))
  else:
    return None