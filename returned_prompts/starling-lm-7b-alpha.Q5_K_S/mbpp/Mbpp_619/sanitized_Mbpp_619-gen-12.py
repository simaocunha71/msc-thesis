def move_num(s: str) -> str:
  return ''.join(c for c in s if not c.isdigit()) + ''.join(c for c in s if c.isdigit())