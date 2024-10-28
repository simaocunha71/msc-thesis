def extract_values(s: str) -> list:
  result = []
  start = False
  for char in s:
      if char == '"':
          start = not start
          continue
      if start:
          result.append(char)
  return result

