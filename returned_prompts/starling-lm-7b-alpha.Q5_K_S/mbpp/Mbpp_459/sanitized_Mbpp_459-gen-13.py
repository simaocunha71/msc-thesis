def remove_uppercase(s: str) -> str:
  return ''.join([c for c in s if not c.isupper()])