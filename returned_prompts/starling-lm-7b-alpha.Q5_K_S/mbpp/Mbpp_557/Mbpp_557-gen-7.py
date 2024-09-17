
def toggle_string(s: str) -> str:
  return ''.join(c.upper() if c.islower() else c.lower() for c in s)


