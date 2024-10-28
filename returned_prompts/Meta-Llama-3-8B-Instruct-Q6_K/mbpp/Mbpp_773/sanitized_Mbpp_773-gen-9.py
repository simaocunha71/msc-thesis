def occurance_substring(s, sub):
  try:
    start = s.index(sub)
    end = start + len(sub)
    return sub, start, end
  except ValueError:
    return None