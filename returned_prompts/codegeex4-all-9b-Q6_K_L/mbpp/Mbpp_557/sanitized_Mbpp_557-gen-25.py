def toggle_string(s):
  return "".join([c.upper() if c.islower() else c.lower() for c in s])