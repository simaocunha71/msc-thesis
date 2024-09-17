
def occurance_substring(string: str, substring: str) -> tuple:
  occurrence = string.find(substring)
  if occurrence == -1:
      return None
  else:
      return (substring, occurrence)


