def is_decimal(s: str) -> bool:
  return s.replace('.', '', 2).isdigit()