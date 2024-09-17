def occurance_substring(s, sub):
  start = s.find(sub)
  if start == -1:
    return None
  else:
    return (sub, start, start+len(sub))