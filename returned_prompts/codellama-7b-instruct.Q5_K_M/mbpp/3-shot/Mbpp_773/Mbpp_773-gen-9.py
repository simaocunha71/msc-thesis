
def occurance_substring(string: str, substring: str) -> tuple:
  if substring in string:
    index = string.index(substring)
    return (substring, index, index+len(substring))
  else:
    return None


