def remove_uppercase(s: str) -> str:
  return ''.join(char if char.islower() else '' for char in s)  # or ''.join(c for c in s if c.islower())