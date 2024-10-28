
def occurance_substring(string: str, substring: str) -> tuple:
  pos = string.find(substring)
  if pos != -1:
    return (substring, pos, pos+len(substring))
  else:
    return None


