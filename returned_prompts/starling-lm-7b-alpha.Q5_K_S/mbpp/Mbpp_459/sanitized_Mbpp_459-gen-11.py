def remove_uppercase(s: str) -> str:
  return ''.join(ch for ch in s if ch.islower())