def extract_quotation(s):
  result = []
  start = False
  for c in s:
    if c == '"':
      start = not start
      if start:
        continue
      result.append(''.join(temp))
      temp = []
    elif start:
      temp.append(c)
  return result