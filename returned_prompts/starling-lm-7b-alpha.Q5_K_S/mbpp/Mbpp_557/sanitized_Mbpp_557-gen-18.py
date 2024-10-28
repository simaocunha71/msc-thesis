def toggle_string(string: str) -> str:
  result = ""
  for c in string:
    if c.isupper():
      result += c.lower()
    else:
      result += c.upper()
  return result