def extract_quotation(s: str) -> list:
  start = 0
  end = 0
  result = []
  while end < len(s):
    if s[end] == '"':
      if start != end:
        result.append(s[start+1:end])
      start = end+1
    end += 1
  return result