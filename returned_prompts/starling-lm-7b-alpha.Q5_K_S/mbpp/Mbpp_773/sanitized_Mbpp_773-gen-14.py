def occurance_substring(s:str,substring:str)->tuple:
  if substring in s:
    return (substring, s.find(substring), s.find(substring)+len(substring))
  else:
    return None