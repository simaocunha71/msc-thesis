def occurance_substring(string:str,substring:str)->tuple:
  start = string.find(substring)
  if start == -1:
    return None
  return (substring, start, start + len(substring) - 1)