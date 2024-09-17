def remove_odd(s: str) -> str:
  return ''.join([c for c in s if s.index(c) % 2 == 0])